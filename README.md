Graduation project!

One repository, two django projects.

Docker, gocker-copose, nginx, postgres, redis, rabbitmq, celery, mailhog.

Warehouse - admin and api. The storekeeper should be able to add books (book instances) through the admin and process incoming orders. Api - used by the store to create an order. Uses first base.

Shop - registration, filtering books, filling the basket, placing an order. Uses second base. There is caching.

Celery - periodically synchronizes the availability of books from the warehouse to the store.

Mailhog - receives mail for the user that the order has been placed and that the order has been completed.