import capsolver
# 
def solve_captcha(websitePublicKey, websiteURL, funcaptchaApiJSSubdomain, blob_data, useragent, proxy, capsolver_apikey, APP_ID):
        # Read https://www.capsolver.com/blog/FunCaptcha/funcaptcha-data-blob to learn about blob_data

        capsolver.api_key = capsolver_apikey # Add Your Capsolver API key here

        data = {
                        "type":"FunCaptchaTaskProxyLess", 
                        "websitePublicKey":  websitePublicKey,
                        "websiteURL": websiteURL,
                        "funcaptchaApiJSSubdomain": funcaptchaApiJSSubdomain,
                        "data": blob_data,
                        'userAgent': useragent,
                        'AppID': APP_ID,
                }

        #print("data", data)
        solution = capsolver.solve(data)

        return solution['token']
