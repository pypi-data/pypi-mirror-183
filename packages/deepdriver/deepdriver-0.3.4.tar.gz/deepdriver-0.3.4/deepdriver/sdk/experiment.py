import re
from typing import Dict
from urllib.parse import urljoin

import deepdriver
from deepdriver import logger
from deepdriver import util
from deepdriver.sdk.config import Config
from deepdriver.sdk.data_types.run import set_run, Run
from deepdriver.sdk.interface import interface


# 실행과 실험환경을 만드는 함수
@util.login_required
def init(exp_name: str = "", team_name: str = "", run_name: str = "", config: Dict = None) -> Run:
    # team_name 변수 vailidation
    pattern = re.compile('[^a-zA-Z0-9._]+')
    if pattern.findall(exp_name):
        logger.info("init() failed : team_name은 숫자(number), 영문자(alphabet), 언더바(_), 온점(.)만 가능합니다.")
        return None

    rsp = interface.init(exp_name, team_name, run_name, config)
    run_url = urljoin(f"http://{interface.get_http_host_ip()}:9111", rsp['runUrl'])
    run = Run(rsp["teamName"], rsp["expName"], rsp["runName"], rsp["runId"], run_url)
    logger.info("DeepDriver initialized\n"
                f"Team Name={rsp['teamName']}\n"
                f"Exp Name={rsp['expName']}\n"
                f"Run Name={rsp['runName']}\n"
                f"Run URL={run_url}"
                )
    set_run(run)

    # init config
    deepdriver.config = Config()
    if config:
        for key, value in config.items():
            setattr(deepdriver.config, key, value)

    return run


@util.login_required
def create_hpo(exp_name: str = "", team_name: str = "", hpo_config: Dict = None) -> Run:
    # hpo_config['parameters']를 REST API스펙에 맞게 key-value 형식으로 변환
    if hpo_config and 'parameters' in hpo_config:
        parameters_dict = hpo_config['parameters']
        key_value_parameters_list = []
        for key, value in parameters_dict.items():
            key_value_dict = {
                "key": key,
                "value": {
                    next(iter(value.keys())): next(iter(value.values()))
                }
            }
            key_value_parameters_list.append(key_value_dict)
        hpo_config['parameters'] = key_value_parameters_list

    rsp = interface.create_hpo(exp_name, team_name, hpo_config)
    logger.info("HPO initialized\n"
                f"Team Name={rsp['teamName']}\n"
                f"Exp Name={rsp['expName']}\n"
                f"Exp Url={rsp['expUrl']}"
                )
    return rsp['result'], rsp['expId']
