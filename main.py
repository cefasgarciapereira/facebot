from FaceBot import FaceBot
import secrets
import pprint

facebot = FaceBot(secrets.username, secrets.password)
facebot.login()
post_ids = ['3117158961628521', '3295830967146135', '4010125388999766', '106631084293442', '1203940519963756']

for post_id in post_ids:
    post_info = facebot.post_info(id=post_id)
    pprint.pprint(post_info)

facebot.logout()