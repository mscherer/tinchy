import bottle
import random
import shelve

def generate_tinchy_id():
    return ''.join(random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
                                 'abcdefghijklmnopqrstuvwxyz' + \
                                 '1234567890', 3))

@bottle.route('/')
def index():
    return '''
    <html>
    <head>
        <title>ManageIQ Talk URL Shortener</title>
        <link href='/images/favicon.ico' rel='shortcut icon'>
    </head>
    <body>
    <h1>Get your shortened ManageIQ Talk URL!</h1>
    <form method="post">
        <input type="text" name="url" style="width: 400px" value="http://talk.manageiq.org" />
        <input type="submit" value="Make it short!" />
    </form>
    </body>
    </html>
    '''

@bottle.post('/')
def make_tinchy_url():
    fatty_url = bottle.request.POST.get('url', '')
    if fatty_url[:24] == 'http://talk.manageiq.org' or fatty_url[:25] == 'https://talk.manageiq.org':
        storage = shelve.open('tinchy')
        tinchy_id = generate_tinchy_id()
        while tinchy_id in storage:
            tinchy_id = generate_tinchy_id()
        storage[tinchy_id] = fatty_url
        storage.close()
        return  '''Your shortened ManageIQ Talk URL is: <a href="{0}">{0}</a>
                '''.format('http://miq.wtf/' + tinchy_id)
    return  '''Boo, <a href="{0}">enter a proper talk.manageiq.org URL this time</a>.
            '''.format('http://miq.wtf/')

@bottle.route('/<tinchy_id>')
def redirect_to_fatty_url(tinchy_id):
    storage = shelve.open('tinchy')
    if tinchy_id not in storage:
        storage.close()
        return 'Nope, this shortened URL was not found.'
    fatty_url = storage[tinchy_id]
    storage.close()
    bottle.redirect(fatty_url)

bottle.run(host='0.0.0.0', port=8080)
