from jwt.jwks import JWKS
from jwt.jwt import JWT
import os
import traceback

try:
    jwks = JWKS(os.environ['OKTA_ISSUER_URI'] + '/v1/keys')
    token = 'eyJraWQiOiJCcTJqc1JSLXJDeFM4aDN2dE9Ib2JUZDJVZEFSZDAzSHdJUmdCOFByUllJIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULmVaOVpMSXV1aWVaR3A4c3FPSjVoalJxbnVsM2xSQWJUdmhwVFZPV21SS0kiLCJpc3MiOiJodHRwczovL2Rldi00MzYyNTYub2t0YS5jb20vb2F1dGgyL2RlZmF1bHQiLCJhdWQiOiJhcGk6Ly9kZWZhdWx0IiwiaWF0IjoxNjA2MTMzMjI5LCJleHAiOjE2MDYxMzY4MjksImNpZCI6IjBvYWF2c3FwMllGUlJUTDV4NWQ1IiwidWlkIjoiMDB1NnloODhWcEFSbzdpdVg1ZDUiLCJzY3AiOlsib3BlbmlkIiwiZW1haWwiXSwic3ViIjoicGhpbGxpcC5lZHdhcmRzQHRvcHRhbC5jb20ifQ.LzZLlgHqXzhtm-garhgYRfvqFLuy2M2gKMJ-8nkaUxHRkvKoE9zp4S4Kr0ReRThQCB8oa5dexqnXpvena1eWMAWrF31ATSCaCAjhfNjp-Y4z-wwj312AKRvhJghKfymIo-rx8Yh6_stf3Y0ZsdYvCo1ORgQ5vjzOzH5VzKrkkl1qL5Zau0FB0Ot4jQFSMYXbYsQEm9XFpaD65wGyEoKwd940ZXakFQfJEB_ooWDlgDjhoKtiZWuC7GAUozNPOEmCmqfCB-IV0U-VLIaZzFOGS3I42up59gu3Xy18nY3ZvznuinZcD7vuetu33CQ8nSMajd3LrkRKLzgZWTQjue0GkQ'
    claims = { 'iss': os.environ['OKTA_ISSUER_URI'], 'aud': 'api://default' }
    jwt = JWT(token, claims, 7)
    print(jwt)
    jwks.verify(jwt)
except Exception as e:
    print('Exception', e)