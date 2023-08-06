# -*- coding: utf-8 -*-
# @time: 2022/12/5 9:42
# @author: Dyz
# @file: base_settings.py
# @software: PyCharm
# 配置文件
import json
import os
import platform

from dutools.exceptions import ConfigurationError


def get_env() -> bool:
    """判断当前运行环境"""
    system = platform.system()
    if system == 'Linux':
        # 生产环境
        return True
    return False


class BaseSettings:
    """
    配置 基类
        判断环境
        覆盖 print 颜色
        yml配置文件
         develop:
              es:
                ...
              mysql:
                host: 127.0.0.1
                ...
              pgsql:
                ...

            public:
              es:
                ...
              mysql:
                host: 127.0.0.1
                ...
    """

    def __init__(self, config_file, base_dir):
        _, extension = os.path.splitext(config_file)
        self.base_dir = base_dir
        if extension in (".yml", ".yaml"):
            import yaml
            with open(os.path.join(base_dir, config_file), "r", encoding='utf-8') as f:
                config = yaml.safe_load(f)
        else:
            raise ConfigurationError('请使用 .yml 或 .yaml 格式!')

        if get_env():
            self.config = config['public']
            self.color = "\033[0;32m{}\033[0m"
            print(self.color.format('生产环境'))
        else:
            self.config = config['develop']
            self.color = "\033[0;34m{}\033[0m"
            print(self.color.format('开发环境'))

    def print(self, string):
        print(self.color.format(string))


class EsSettings(BaseSettings):
    """yml配置文件
        conf.yml

          develop:
              es:
                index: bios
                hosts:
                  - http://127.0.0.1:9200
                mapping_file: bios.json
              mysql:
                host: 127.0.0.1
                port: 3306
                user: root
                password: 123456
                database: db
                charset: utf8mb4
              pgsql:
                host: 127.0.0.1
                port: 5432
                user: postgres
                pwd: 132456

            public:
              es:
                jour_index:
                    journales.json
                mesh_index:
                    meshes.json
                hosts:
                  - http://127.0.0.1:9200
                mapping_file:
                    - journales.json
                    - meshes.json
              mysql:
                host: 127.0.0.1
                port: 3306
                user: root
                password: 123456
                database: db
                charset: utf8mb4
    """

    def __init__(self, config_file, base_dir):
        super().__init__(config_file, base_dir)

        from elasticsearch import Elasticsearch

        self.es: Elasticsearch = Elasticsearch(hosts=self.config['es']['hosts'])
        self.index: str = self.config['es']['index']
        es_mapping = self.config['es'].get('mapping_file')
        if es_mapping:
            if isinstance(es_mapping, list):
                self.es_mapping = [i.split('.json')[0] for i in es_mapping]
            else:
                self.es_mapping = es_mapping.split('.json')[0]

        self.es_ip = self.config['es']['hosts']

    def cat(self, sta=False, index_conf=None):
        self.print(self.config['es'])
        if sta:
            if not index_conf.endswith('.json'):
                index_conf += '.json'
            index_conf_path = os.path.join(self.base_dir, index_conf)
            with open(index_conf_path, "r") as f:
                es_index_settings = json.load(f)
            self.print(es_index_settings)

    def _create_index(self, index=None, index_conf=None):
        """创建索引"""
        if not index and isinstance(self.index, str):
            index = self.index
        elif not index:
            raise ConfigurationError('无索引参数,或有多个索引， 请指定索引: index_conf=')
        if not index_conf and self.es_mapping:
            if isinstance(self.es_mapping, list):
                raise ConfigurationError('ES配置文件有多个！ 请指定文件: index_conf=')
            else:
                index_conf = self.es_mapping

        if not index_conf.endswith('.json'):
            index_conf += '.json'
        index_conf_path = os.path.join(self.base_dir, index_conf)
        with open(index_conf_path, "r") as f:
            es_index_settings = json.load(f)
        resp = self.es.indices.create(index=index, body=es_index_settings)
        self.print(resp)

    def _delete_index(self, index=None):
        """删除索引"""
        if not index and isinstance(self.index, str):
            index = self.index
        elif not index:
            raise ConfigurationError('无索引参数,或有多个索引， 请指定索引: index_conf=')
        s = input(f'正在删除索引, 地址: {self.es_ip}索引名: {index}  是否执行 (y/n):')
        if s.lower() == 'y':
            resp = self.es.indices.delete(index=index)
            self.print(resp)

    def _clear(self, index=None):
        """清空当前索引数据"""
        if not index and isinstance(self.index, str):
            index = self.index
        elif not index:
            raise ConfigurationError('无索引参数,或有多个索引， 请指定索引: index_conf=')
        s = input(f'正在清空数据, 地址: {self.es_ip}索引名: {index}  是否执行 (y/n):')
        if s.lower() == 'y':
            body = {'query': {'match_all': {}}}
            resp = self.es.delete_by_query(index=index, body=body)
            self.print(resp)


if __name__ == '__main__':
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    settings = EsSettings('a.yml', BASE_DIR)
    # settings.cat(sta=True, index_conf='journales')
    settings.cat()
    settings._create_index(index='journales', index_conf='journales')
    settings._clear(index='journales')
    settings._delete_index(index='journales')
