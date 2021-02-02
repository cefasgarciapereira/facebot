from FaceBot import FaceBot
import secrets
import pprint

facebot = FaceBot(secrets.username, secrets.password, log=True)
facebot.login()
post_ids = ['3117158961628521', '3295830967146135', '4010125388999766', '106631084293442', '1203940519963756']

for post_id in post_ids:
    facebot.set_post_id(post_id)
    pprint.pprint(facebot.post_info())

facebot.logout()