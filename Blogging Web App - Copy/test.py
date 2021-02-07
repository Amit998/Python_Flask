import os
import json
from app import db
from  app.models import User,Post


# user_1=User(username='Test 2',email='test_1@gmail.com',password='12345678')

# db.session.add(user_1)
# db.session.commit()


# print(User.query.all())
post_image='default_post.jpg'

# # print(os.getcwd())
# print(os.path.exists("./app/static/image/Profile_Default/5b36c8d5bdd9e242.jpg"))
# os.remove("./app/static/image/Profile_Default/5b36c8d5bdd9e242.jpg")
    # print('exist')
# else:
#   print("The file does not exist")

# suvo1910


f=open('posts.json',)
posts=json.load(f)

# print(data)

for post in posts:
    title=post['title']
    content=post['content']
    user_id=post['user_id']

    post_add=Post(title=title,content=content,post_image=post_image,user_id=user_id)
    db.session.add(post_add)
    db.session.commit()
    print('added')

    # print(title,content,user_id)

# title,content,picture,user_id