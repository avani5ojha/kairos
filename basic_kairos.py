import kairos_face as kf



kf.settings.app_id='ypur app id'
kf.settings.app_key='your app key'

# galleries_list=kf.get_galleries_names_list()
#
# print(galleries_list)
#
# gallery_sub=kf.get_gallery('a-gallery')
#
# print(gallery_sub)

recognized_faces = kf.detect_face(file='harry-meghan-15.jpg' )
detected_faces = kf.recognize_face(file='harry-meghan-15.jpg' , gallery_name='a-gallery')
