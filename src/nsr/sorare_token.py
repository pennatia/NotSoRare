# Import Necessary Packages
import requests
import json
import bcrypt

## Authentication Function --  Free to be imported into other modules
def authenticate(email, password): # A simple function to use requests.post to make the API call. Note the json= section.

    # Encryption for the Password
    r = requests.get(f"https://api.sorare.com/api/v1/users/{email}")
    pwd = r.json()
    password = password.encode('utf-8')
    salt = pwd['salt'].encode('utf-8')
    hashed_pwd = bcrypt.hashpw(password,salt)
    pwd_input = str(hashed_pwd.decode('utf-8'))


    # Set headers for API Call
    a = r.headers['content-type']
    headers = {'content-type':a}

    # Set Query to Retrieve Token
    mutation = """
    mutation SignInMutation($input: signInInput!) {
        signIn(input: $input) {
            currentUser {
                slug
                jwtToken(aud: "Cost Analysis") {
                    token
                    expiredAt
                }
            }
            errors {
                message
            }
        }
    }"""

    # Mutation Variables
    variables = {"input":{
        "email": email,
        "password": pwd_input
        }
    }
    
    # Request
    request = requests.post('https://api.sorare.com/graphql', json={'query': mutation, 'OperationName': 'SignInMutation', 'variables':variables}, headers=headers)
    output = request.json()["data"]["signIn"]["currentUser"]["jwtToken"]["token"]

    # Return appropriate values or raise exception
    if request.status_code == 200:
        
        # Ask whether we want to save to a text file
        saver = input("Would you like to save your token to a text file? [y/n] \n")

        # Save token to text file
        if saver == 'y':
            text_file = open("Token.txt", "w")
            text_file.write(output)
            text_file.close()
        
        # Otherwise, return
        return output
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, mutation))

