from fastapi import FastAPI


app = FastAPI(title='Test api')


fake_users = [{'id': 1, 'name': 'Bob'},
              {'id': 2, 'name': 'Alex'},
              ]


@app.get('/blog/')
def get_user_blog():
    return {'hello': 'world'}
