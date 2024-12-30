from django.core.management.base import BaseCommand
from django.db import connection
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Initialize database with required tables'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT EXISTS(
                    SELECT FROM pg_tables 
                    WHERE tablename = 'auth_user'
                );
            """)
            table_exists = cursor.fetchone()[0]

        if not table_exists:
            self.stdout.write('Running migrations...')
            call_command('migrate')
            self.stdout.write(self.style.SUCCESS('Successfully initialized database'))
        else:
            self.stdout.write('Database already initialized') 