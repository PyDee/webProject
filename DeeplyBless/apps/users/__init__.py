import pymysql

pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()
default_app_config = 'users.apps.UsersConfig'
