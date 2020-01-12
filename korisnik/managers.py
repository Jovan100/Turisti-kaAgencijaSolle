from django.contrib.auth.models import BaseUserManager

class KorisnikManager(BaseUserManager):
    def create_user(self, ime, prezime, email, broj_telefona, username, password=None, is_active=True, is_staff=False, is_admin=False):
        if not ime:
            raise ValueError('Korisnik mora imati ime.')
        if not prezime:
            raise ValueError('Korisnik mora imati prezime.')
        if not email:
            raise ValueError('Korisnik mora imati email adresu.')
        if not broj_telefona:
            raise ValueError('Korisnik mora imati broj telefona.')
        if not username:
            raise ValueError('Korisnik mora imati korisničko ime.')
        if not password:
            raise ValueError('Korisnik mora imati password.')
        else:
            user = self.model(
                email = self.normalize_email(email),
            )
            user.ime = ime
            user.prezime = prezime
            user.email = email
            user.broj_telefona = broj_telefona
            user.username = username
            user.is_staff = is_staff
            user.is_active = is_active
            user.is_admin = is_admin
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_staffuser(self, ime, prezime, email, broj_telefona, username, password=None):
        user = self.create_user(
            ime,
            prezime,
            email,
            broj_telefona,
            username,
            password=password,
            is_staff = True
        )
        return user

    def create_superuser(self, ime, prezime, email, broj_telefona, username, password=None):
        user = self.create_user(
            ime,
            prezime,
            email,
            broj_telefona,
            username,
            password=password,
            is_staff = True,
            is_admin = True
        )
        return user
