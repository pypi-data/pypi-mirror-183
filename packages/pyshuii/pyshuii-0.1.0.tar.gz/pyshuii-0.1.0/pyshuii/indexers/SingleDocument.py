import uuid
import json
import asyncio
import aiohttp
import ssl
import certifi
import tqdm

from pyshuii.utils import traceCast


class SingleDocument:
    def __init__(self, resource):
        self.resource = resource
        self.SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())
        self.jobs = {}
        self.document = []
        self.results = []

    async def create_job(self, job):
        job_id = uuid.uuid4()
        self.jobs[job_id] = job

        return job_id

    def modify_job(self, job_id, job):
        if not job_id in self.jobs:
            raise Exception("SingleDocument: Invalid job_id")

        self.jobs[job_id] = job

    async def execute_jobs(self, fn):
        async with aiohttp.ClientSession(trust_env=True) as session:
            try:
                async with session.get(self.resource, ssl=self.SSL_CONTEXT) as response:
                    if not response.status == 200:
                        raise Exception(
                            f"SingleDocument: [Status] {response.status}")

                    res = await response.read()
                    self.document = json.loads(res.decode("utf8"))
                    await traceCast(
                        desc="Execute jobs",
                        fn=fn or SingleDocument.retrieve,
                        tasks=[{
                            'document': self.document,
                            'job_id': job_id,
                            'job': self.jobs[job_id],
                            'results': self.results
                        } for job_id in self.jobs]
                    )
                    self.jobs = {}
                    print("SingleDocument: Jobs have been executed")
            except:
                raise Exception("SingleDocument: Unable to retrieve document")

    def clear_results(self):
        self.results = {}

    @ staticmethod
    async def retrieve(document, job_id, job, results):
        try:
            results.append(document[job])
        except Exception as e:
            print(e)
            print(f'SingleDocument: {job_id} - {job}')
