try:
    import aiodagpi
except:
    pass
try:
    import aiohttp
except:
    pass
# Function travis will check to pass / fail build
def test():
    assert aiodagpi, 'Could not import aiodagpi'
    assert aiohttp, 'Could not import aiohttp'
