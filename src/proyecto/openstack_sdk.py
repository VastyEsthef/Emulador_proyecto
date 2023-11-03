import json, requests

# KEYSTONE API
def password_authentication_with_unscoped_authorization(auth_endpoint, user_domain_name, username, password):
    url = auth_endpoint + '/auth/tokens'
    
    data = \
        {
            "auth": {
                "identity": {
                    "methods": [
                        "password"
                    ],
                    "password": {
                        "user": {
                            "name": username,
                            "domain": {
                                "name": user_domain_name
                            },
                            "password": password
                        }
                    }
                }
            }
        }
    
    r = requests.post(url=url, data=json.dumps(data))
    # status_code success = 201
    return r


def password_authentication_with_scoped_authorization(auth_endpoint, user_domain_name, username, password, project_domain_id, project_name):
    url = auth_endpoint + '/auth/tokens'

    data = \
        {
            "auth": {
                "identity": {
                    "methods": [
                        "password"
                    ],
                    "password": {
                        "user": {
                            "name": username,
                            "domain": {
                                "name": user_domain_name
                            },
                            "password": password
                        }
                    }
                },
                "scope": {
                    "project": {
                        "domain": {
                            "id": project_domain_id
                        },
                        "name": project_name
                    }
                }
            }
        }
        
    r = requests.post(url=url, data=json.dumps(data))
    # status_code success = 201
    return r
