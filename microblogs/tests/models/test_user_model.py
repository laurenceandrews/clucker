from django.core.exceptions import ValidationError
from django.test import TestCase
from microblogs.models import User

# Unit tests go here
class UserModelTestCase(TestCase):

    fixtures = [
        'microblogs/tests/fixtures/default_user.json',
        'microblogs/tests/fixtures/other_users.json'
    ]

    def setUp(self):
        self.user = User.objects.get(username='@johndoe')

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
        second_user = User.objects.get(username='@janedoe')
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


    def test_first_name_must_not_be_blank(self):
        self.user.first_name = ''
        self.assert_user_is_invalid()

    def test_first_name_need_not_be_unique(self):
        second_user = User.objects.get(username='@janedoe')
        self.user.first_name = second_user.first_name
        self.assert_user_is_valid()

    def test_first_name_may_contain_50_charaters(self):
        self.user.first_name = 'x' * 50
        self.assert_user_is_valid()

    def test_first_name_must_not_contain_more_than_50_characters(self):
        self.user.first_name = 'x' * 51
        self.assert_user_is_invalid()


    def test_last_name_must_not_be_blank(self):
        self.user.last_name = ''
        self.assert_user_is_invalid()

    def test_last_name_need_not_be_unique(self):
        second_user = User.objects.get(username='@janedoe')
        self.user.last_name = second_user.last_name
        self.assert_user_is_valid()

    def test_last_name_may_contain_50_charaters(self):
        self.user.last_name = 'x' * 50
        self.assert_user_is_valid()

    def test_last_name_must_not_contain_more_than_50_characters(self):
        self.user.last_name = 'x' * 51
        self.assert_user_is_invalid()


    def test_email_must_not_be_blank(self):
        self.user.email = ''
        self.assert_user_is_invalid()

    def test_email_must_be_unique(self):
        second_user = User.objects.get(username='@janedoe')
        self.user.email = second_user.email
        self.assert_user_is_invalid()

    def test_email_must_contain_username(self):
        self.user.email = '@example.org'
        self.assert_user_is_invalid()

    def test_email_must_contain_at_symbol(self):
        self.user.email = 'johndoe.example.org'
        self.assert_user_is_invalid()

    def test_email_must_contain_domain_name(self):
        self.user.email = 'johndoe@.org'
        self.assert_user_is_invalid()

    def test_email_must_contain_domain(self):
        self.user.email = 'johndoe@example'
        self.assert_user_is_invalid()

    def test_email_must_not_contain_more_than_one_at(self):
        self.user.email = 'johndoe@@example.org'
        self.assert_user_is_invalid()


    def test_bio_may_be_blank(self):
        self.user.bio = ''
        self.assert_user_is_valid()

    def test_bio_need_not_be_unique(self):
        second_user = User.objects.get(username='@janedoe')
        self.user.bio = second_user.bio
        self.assert_user_is_valid()

    def test_bio_may_contain_520_characters(self):
        self.user.bio = 'x' * 520
        self.assert_user_is_valid()

    def test_bio_must_not_contain_more_than_520_characters(self):
        self.user.bio = 'x' * 521
        self.assert_user_is_invalid()


    def assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail('Test user should be valid')

    def assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()
