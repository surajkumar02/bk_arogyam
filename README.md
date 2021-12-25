# bk_arogyam
build APIs with Python-Django, DRF.

For linux:

        python3 -m pip install --user virtualenv
        python3 -m venv env
        source env/bin/activate
        
        
For Windows:

          py -m pip install --user virtualenv 
          py -m venv env
          ./env/Scripts/activate OR ./env/Scripts/activate.bat (if not working)
          
Install Dependencies:

          pip install -r requirements.txt
          
Run the Server:
          
          python manage.py runserver
          python manage.py runserver [PORT] (if requires) (eg. python manage.py runserver 10001)
          
       if error:
          python manage.py makemigrations
          python manage.py migrate
          python manage.py createsuperuser
          
        Enter credentials as you want:
        name:
        email:
        password:
        confirm password:
        
        Enjoy:)
        Don't forgot: python manage.py runserver
        
        
      Link for admin panel:
        http://localhost:8000/admin/
            
          
          
urls:

   http://localhost:8000/ 
   APIs:
   
       'api/register/'
       'api/login/'
       'api/blog/'
       'api/blog/<int:pk>/'
       'api/comment/<int:pk>'
       'api/<int:blog>/comments/'
       'api/like/<int:blog>/<int:user>'
       
 Details of API:
 
    1. Register User
    2. Login User
    3. Create Blog
    4. Modify Blog
    5. Delete Blog
    6. List all blogs (pagination (list of 5)+ Likes Count + Comments Count)
    7. View Single Blog (latest 5 comments + Likes Count +Comments count)
    8. Like a blog / Unlike a blog
    9. Comment on a blog
    10. List of all comments on a blog (along with pagination)
    
       
Credentials:

username:admin

pass:test@123
