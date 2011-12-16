import bottle, random, shelve

def generate_tinchy_id():
    return ''.join( random.sample( 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890' , 3 ) )

@bottle.route('/')
def index():
    return """
    <h1>Get your tinchy URL!</h1>
    <form method="post">
      <input type="text" name="url" value="http://" />
      <input type="submit" value="Make it tinchy!" />
    </form>
    """

@bottle.post('/')
def make_tinchy_url():
    fatty_url = request.POST.get( 'url' , '' )
    if fatty_url[:7] == 'http://':
        storage = shelve.open( 'tinchy' )
        tinchy_id = generate_tinchy_id()
        while storage.has_key( tinchy_id ):
            tinchy_id = generate_tinchy_id()
        storage[tinchy_id] = fatty_url
        storage.close()
        return 'Your tinchy url is: <a href="%s">%s</a>' % ( request.url + tinchy_id )
    return 'Boo, <a href="%s">enter a proper url this time</a>.' % request.url

@bottle.route('/<tinchy_id>')
def redirect_to_fatty_url( tinchy_id ):
    storage = shelve.open( 'tinchy' )
    if tinchy_id not in storage:
        storage.close()
        return "Nope, this tinchy URL wasn't found." 
    storage.close()
    redirect( storage[tinchy_id] )
    
bottle.run(host='0.0.0.0', port=80)