from models import Playlist, Song, PlaylistSong, db
from app import app

db.drop_all()
db.create_all()

Playlist.query.delete()
Song.query.delete()
PlaylistSong.query.delete()

p1 = Playlist(name='70s Rock', description='Best rock songs')
s1= Song(title='Stairway to Heaven', artist='Led Zeppelin')
s2= Song(title='Black Dog', artist ='Led Zeppelin')
s3= Song(title='Hotel California', artist ='Eagles')
s4= Song(title='Take It Easy', artist ='Eagles')
s5= Song(title='Go Your Own Way',artist ='Fleetwood Mac')

db.session.add_all([p1,s1,s2,s3,s4,s5])
db.session.commit()

ps1 = PlaylistSong(playlist_id = p1.id, song_id=s1.id)
ps2 = PlaylistSong(playlist_id = p1.id, song_id=s2.id)
ps3 = PlaylistSong(playlist_id = p1.id, song_id=s3.id)
ps4 = PlaylistSong(playlist_id = p1.id, song_id=s4.id)
ps5 = PlaylistSong(playlist_id = p1.id, song_id=s5.id)

db.session.add_all([ps1,ps2,ps3,ps4,ps5])
db.session.commit()