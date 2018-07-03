import kairos_face as kf

# kf.settings.app_id='7fa6bda7'
# kf.settings.app_key='0a782b95e6fb05aa932e55f4bcc47453'

kf.settings.app_id='7fa6bda7'
kf.settings.app_key='0a782b95e6fb05aa932e55f4bcc47453'

# galleries_list=kf.get_galleries_names_list()
#
# print(galleries_list)
#
# gallery_sub=kf.get_gallery('a-gallery')
#
# print(gallery_sub)

recognized_faces = kf.detect_face(file='harry-meghan-15.jpg' )
detected_faces = kf.recognize_face(file='harry-meghan-15.jpg' , gallery_name='a-gallery')
