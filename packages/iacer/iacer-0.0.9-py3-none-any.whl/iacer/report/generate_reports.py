import asyncio
import datetime
import logging
import os
import textwrap
import time
from pathlib import Path

import aiofiles
import tabulate
import yattag

from iacer.stack import Stacker, Stack

LOG = logging.getLogger(__name__)


class ReportBuilder:
    """
    This class generates the test report.
    """

    def __init__(self, stacks: Stacker, output_file: Path):
        self._stacks = stacks
        self._output_file = output_file

    async def generate_report(self):
        doc = yattag.Doc()

        tag = doc.tag
        text = doc.text
        dirname = os.path.abspath(os.path.dirname(__file__))
        async with aiofiles.open(f'{dirname}/html.css', 'r') as f:
            output_css = await f.read()

        with tag("html"):
            with tag("head"):
                doc.stag("meta", charset="utf-8")
                doc.stag("meta", name="viewport", content="width=device-width")
                with tag("style", type="text/css"):
                    text(output_css)
                with tag("title"):
                    text("Iacer Report")

            with tag("body"):
                tested_on = time.strftime("%A - %b,%d,%Y @ %H:%M:%S")

                with tag("table", "class=header-table-fill"):
                    with tag("tbody"):
                        with tag("th", "colspan=2"):
                            with tag("tr"):
                                with tag("td"):
                                    text("Tested on: ")
                                    text(tested_on)
            doc.stag("p")
            with tag("table", "class=table-fill"):
                with tag("tbody"):
                    with tag("thread"):
                        with tag("tr"):
                            with tag("th", "class=text-center", "width=25%"):
                                text("Test Name")
                            with tag("th", "class=text-left", "width=10%"):
                                text("Tested Region")
                            with tag("th", "class=text-left", "width=30%"):
                                text("Stack Name")
                            with tag("th", "class=text-left", "width=20%"):
                                text("Tested Results")
                            with tag("th", "class=text-left", "width=15%"):
                                text("Test Logs")

                            for stack in self._stacks.stacks:
                                with tag("tr", "class= test-footer"):
                                    with tag("td", "colspan=5"):
                                        text("")

                                LOG.info(f"Reporting on {str(stack.id)}")
                                test_name = stack.test_name
                                status = stack.status
                                stack_name = stack.name
                                region = stack.region
                                css = "class=test-green" if status == 'CREATE_COMPLETE' else 'class=test-red'

                                with tag("tr"):
                                    with tag("td", "class=test-info"):
                                        with tag("h3"):
                                            text(test_name)
                                    with tag("td", "class=text-left"):
                                        text(region)
                                    with tag("td", "class=text-left"):
                                        text(stack_name)
                                    with tag("td", css):
                                        text(str(status))
                                    with tag("td", "class=text-left"):
                                        clog = f"{stack_name}-{region}.txt"
                                        with tag("a", href=clog):
                                            text("View Logs ")
                        doc.stag("p")

            html_output = yattag.indent(
                doc.getvalue(), indentation="    ", newline="\r\n", indent_text=True
            )
            async with aiofiles.open(str(self._output_file / 'index.html'), "w", encoding="utf-8") as _f:
                await _f.write(html_output)
            return html_output

    async def get_events(self, stack: Stack):
        stack_events = await stack.events(refresh=True)
        events = []
        for event in stack_events:
            event_details = {
                "TimeStamp": str(event.timestamp),
                "ResourceStatus": event.status,
                "ResourceType": event.type,
                "LogicalResourceId": event.logical_id,
            }
            if event.status_reason:
                event_details["ResourceStatusReason"] = event.status_reason
            else:
                event_details["ResourceStatusReason"] = ""

            events.append(event_details)
        return events

    async def create_logs(self):
        tasks = []
        for stack in self._stacks.stacks:
            file_name = f'{stack.name}-{stack.region}.txt'
            task = asyncio.create_task(self.write_logs(stack, self._output_file / file_name))
            tasks.append(task)
        await asyncio.gather(*tasks)

    async def write_logs(self, stack: Stack, log_path: Path):
        stack_name = stack.name
        region = stack.region

        events = await self.get_events(stack) if stack.id else []

        if stack.launch_succeeded:
            tested_result = 'Success'
            reason = 'Stack launch was successful'
        else:
            tested_result = 'Failed'
            reason = f'{stack.status}, {stack.status_reason}'

        async with aiofiles.open(str(log_path), "a", encoding="utf-8") as log_output:
            await log_output.write(
                "------------------------------------------------------------------"
                "-----------\n"
            )
            await log_output.write("Region: " + region + "\n")
            await log_output.write("StackName: " + stack_name + "\n")
            await log_output.write(
                "******************************************************************"
                "***********\n"
            )
            await log_output.write(f"TestedResult: {tested_result}  \n")
            await log_output.write("ResultReason:  \n")
            await log_output.write(textwrap.fill(str(reason), 85) + "\n")
            await log_output.write(
                "******************************************************************"
                "***********\n"
            )
            await log_output.write(
                "******************************************************************"
                "***********\n"
            )
            await log_output.write("Events:  \n")
            await log_output.writelines(tabulate.tabulate(events, headers="keys"))
            await log_output.write(
                "\n****************************************************************"
                "*************\n"
            )
            await log_output.write(
                "------------------------------------------------------------------"
                "-----------\n"
            )
            await log_output.write(
                "Tested on: "
                + datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p")
                + "\n"
            )
            await log_output.write(
                "------------------------------------------------------------------"
                "-----------\n\n"
            )
            await log_output.close()
