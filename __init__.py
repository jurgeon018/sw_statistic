from django import apps 


class StaticticConfig(apps.AppConfig):
    name = 'sw_show.sw_statistic'
    verbose_name = 'Статистика'

default_app_config = 'sw_shop.sw_statistic.StaticticConfig'


