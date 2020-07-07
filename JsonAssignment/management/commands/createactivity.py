from django.core.management.base import BaseCommand
from JsonAssignment.models import ActivityPeriod, User
class Command(BaseCommand):
    help = 'Create Users and Activity plans from yaml'
    def handle(self, *args, **options):
        #Creating user1 and his activities
        u1=User(uid='W012HAMH112', real_name='Idris', tz='Gurgaon/India')
        a1=ActivityPeriod(uid=u1, start_time='Feb 1 2020  1:33PM', end_time='Feb 1 2020 1:54PM')
        a2=ActivityPeriod(uid=u1, start_time='Mar 1 2020  11:11AM', end_time='Mar 1 2020 2:00PM')
        a3=ActivityPeriod(uid=u1, start_time='Mar 16 2020  5:33PM', end_time='Mar 16 2020 8:02PM')
        u1.save()
        a1.save()
        a2.save()
        a3.save()

        #Creating user2 and his activities
        u2=User(uid='W032HAMH332', real_name='Donald Trump', tz='California/United States')
        a4=ActivityPeriod(uid=u2, start_time='Feb 1 2020  1:33PM', end_time='Feb 1 2020 1:54PM')
        a5=ActivityPeriod(uid=u2, start_time='Mar 1 2020  11:11AM', end_time='Mar 1 2020 2:00PM')
        a6=ActivityPeriod(uid=u2, start_time='Mar 16 2020  5:33PM', end_time='Mar 16 2020 8:02PM')
        u2.save()
        a4.save()
        a5.save()
        a6.save()

        #Creating user3 and his activities
        u3=User(uid='W092HAMH992', real_name='Kanye West', tz='Arizona/United States')
        a7=ActivityPeriod(uid=u3, start_time='Feb 1 2020  1:33PM', end_time='Feb 1 2020 1:54PM')
        a8=ActivityPeriod(uid=u3, start_time='Mar 1 2020  11:11AM', end_time='Mar 1 2020 2:00PM')
        a9=ActivityPeriod(uid=u3, start_time='Mar 16 2020  5:33PM', end_time='Mar 16 2020 8:02PM')
        u3.save()
        a7.save()
        a8.save()
        a9.save()


        self.stdout.write(self.style.SUCCESS('Successfully created Activities for the specified Users'))