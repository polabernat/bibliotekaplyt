from django.test import TestCase
from .models import User,
from django.contrib.auth.models import User, Permission

# Create your tests here.
#Główne funkcjonalności aplikacji, powinny być pokryte testami
# (co najmniej 3 testy jednostkowe napisane przy użyciu pytest'a).
# Do każdego widoku powinny być co najmniej dwa testy.



from django.utils import timezone

from .models import History, Band, Album

class HistoryModelTests(TestCase):
    def test_was_published_recently_with_update(self):
        time = timezone.now() + datetime.timedelta(days=30)
        update = History(pub_date=time)
        self.assertIs(update.was_published_recently(), False)


class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        response = self.client.get('your_server_ip:8000')
        self.assertEqual(response.status_code, 200)

class BandModelTest(TestCase):
    def band_name_max_length(self):
        band = Band.objects.get
        max_length = band._meta.get_field('band_name').max_length
        self.assertEqual(max_length, 64)

class AlbumModelTest(TestCase):
    def album_name_max_length(self):
        album = Album.objects.get
        max_length = album._meta.get_field('band_name').max_length
        self.assertEqual(max_length, 64)

class Connected(TestCase):
    def process_request(self, request):
        try:
            "SELECT * FROM Band"
            success = True
        except:
            success = False
        request.db_connection_successful = success

class UserLogged(TestCase):
    def process_request(self, request):
        try:
            "SELECT name FROM auth_user WHERE name='Dudek'"
            success = True
        except:
            success = False
        request.db_connection_successful = success

@pytest.mark.django_db
def test_add_song_missing_permission(user, unauthorised_user, test_user):
    user.force_login(unauthorised_user)
    response = user.post('/add-song', {})
