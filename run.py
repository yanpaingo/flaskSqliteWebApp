from flaskBlog import create_app

app = create_app()

if __name__ == '__main__':
    website_url = 'mysite.pai:5000'
    app.config['SERVER_NAME'] = website_url
    app.run( debug=True)