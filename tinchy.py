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
    <h1>Get your tinchy URL!</h1>
    <form method="post">
        <input type="text" name="url" value="http://" />
        <input type="submit" value="Make it tinchy!" />
    </form>
    '''


@bottle.post('/')
def make_tinchy_url():
    fatty_url = bottle.request.POST.get('url', '')
    if fatty_url[:7] == 'http://' or fatty_url[:8] == "https://:
        storage = shelve.open('tinchy')
        tinchy_id = generate_tinchy_id()
        while tinchy_id in storage:
            tinchy_id = generate_tinchy_id()
        storage[tinchy_id] = fatty_url
        storage.close()
        return  '''Your tinchy url is: <a href="{0}">{0}</a>
                '''.format(bottle.request.url + tinchy_id)
    return  '''Boo, <a href="{0}">enter a proper url this time</a>.
            '''.format(bottle.request.url)


@bottle.route('/<tinchy_id>')
def redirect_to_fatty_url(tinchy_id):
    storage = shelve.open('tinchy')
    if tinchy_id not in storage:
        storage.close()
        return 'Nope, this tinchy URL was not found.'
    fatty_url = storage[tinchy_id]
    storage.close()
    bottle.redirect(fatty_url)

bottle.run(host='0.0.0.0', port=80)
