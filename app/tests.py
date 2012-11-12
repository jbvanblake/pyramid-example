import unittest
import transaction

from pyramid import testing

from .models import DBSession

from .models import (
    Base,
    MyModel,
    Route,
    Stop,
    )

class TestMyView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            route= Route(route_number=2)
            DBSession.add(route)
            DBSession.flush()

            stop = Stop(stop_number=3, route_id = route.route_id)
            DBSession.add(stop)
            model = MyModel(name='one', value=55)
            DBSession.add(model)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_it(self):
        from .views import my_view
        request = testing.DummyRequest()
        stop = DBSession.query(Stop).filter(Stop.stop_number==3).first()
        assert stop
        info = my_view(request)
        self.assertEqual(info['one'].name, 'one')
        self.assertEqual(info['project'], 'app')
