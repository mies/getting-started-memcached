import os
import memcache

client = memcache.Client([os.getenv('WERCKER_MEMCACHED_HOST')], debug=True)
mapping = {'foo': 'FOO', 'bar': 'BAR'}
bad_keys = client.set_multi(mapping)
print self.assertEqual(sorted(bad_keys), ['bar', 'foo'])
if DEBUG:
  print 'set_multi({0!r}) -> {1!r}'.format(mapping, bad_keys)

