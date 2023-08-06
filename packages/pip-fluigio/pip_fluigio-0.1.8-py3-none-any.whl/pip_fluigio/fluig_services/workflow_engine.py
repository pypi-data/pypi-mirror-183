from typing import List, Optional

from pip_fluigio.__fluig_services_base.workflow_engine import WorkflowEngineProvider
from pip_fluigio.__fluig_services_base.interfaces.workflow_engine import (
    Attachments,
    Colleagues,
    SaveAndSendTaskClassic,
    CardData,
    Item
)
from pip_fluigio.fluig_services.infraestruture.server import ClientFluig

from pip_fluigio.utils.logger import Logger


class WorflowEngine(WorkflowEngineProvider):
    def __init__(self, wsdl_url: str, client: Optional[ClientFluig] = None):
        self._client = client or ClientFluig(wsdl_url=wsdl_url)
        self._logger = Logger()

    def save_and_send_task(
        self,
        *,
        company_id: str,
        user_name: str,
        password: str,
        colleague_name: str,
        description: str,
        attachments: List[Attachments],
        colleague_ids: List[Colleagues],
        items: list[Item],
        choosed_state: str,
        comments: str,
        user_id: str,
        complete_task: str,
        process_instance_id: str,
        manager_mode: str,
        thread_sequence: str,
    ) -> None:

        try:
            self._logger.attribute.info(f"Start request save and send task")

            response = self._client.soap_intance.service.saveAndSendTaskClassic(
                company_id,
                user_name,
                password,
                SaveAndSendTaskClassic(           
                    colleague_name=colleague_name,
                    colleague_ids=[colleague for colleague in colleague_ids], 
                    description=description,
                    choosed_state=choosed_state,
                    complete_task=complete_task,
                    comments=comments,
                    user_id=user_id,
                    process_instance_id=process_instance_id,
                    manager_mode=manager_mode,
                    thread_sequence=thread_sequence,
                    attachments= [attach for attach in attachments],
                    card_data=CardData(item=items),
                ).dict(),
            )

            return

        except Exception as error:
            self._logger.attribute.error(error)

        return
