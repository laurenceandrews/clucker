from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import User

# Unit tests go here
class UserModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            '@johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.org',
            password='Password123',
            bio='The quick brown fox jumps over the lazy dog.'
        )

    def test_valid_user(self):
        self.assert_user_is_valid()

    def test_username_cannot_be_blank(self):
        self.user.username = ''
        self.assert_user_is_invalid()

    def test_username_can_be_30_characters_long(self):
        self.user.username = '@' + 'x' * 29
        self.assert_user_is_valid()

    def test_username_cannot_be_over_30_characters_long(self):
        self.user.username = '@' + 'x' * 30
        self.assert_user_is_invalid()

    def test_username_must_be_unique(self):
        second_user = self.create_second_user()
        self.user.username = second_user.username
        self.assert_user_is_invalid()

    def test_username_must_start_with_at_symbol(self):
        self.user.username = 'johndoe'
        self.assert_user_is_invalid()

    def test_username_must_contain_only_alphanumericals_after_at(self):
        self.user.username = '@john!doe'
        self.assert_user_is_invalid()

    def test_username_must_contain_at_least_3_alphanumericals_after_at(self):
        self.user.username = '@jo'
        self.assert_user_is_invalid()

    def test_username_may_contain_numbers(self):
        self.user.username = '@j0hndoe2'
        self.assert_user_is_valid()

    def test_username_must_contain_only_one_at(self):
        self.user.username = '@@johndoe'
        self.assert_user_is_invalid()

    def assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail('Test user should be valid')

    def test_first_name_must_not_be_blank(self):
        pass

    def test_first_name_need_not_be_unique(self):
        pass

    def test_first_name_may_contain_50_charaters(self):
        pass



    def assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

    def create_second_user(self):
        User.objects.create_user(
            '@janedoe',
            first_name='Jane',
            last_name='Doe',
            email='janedoe@example.org',
            password='Password123',
            bio="This is Jane's profile."
        )
        return user
