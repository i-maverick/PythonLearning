import asyncio
import os
import requests
import time

async def download(url):
    print('Downloading file {0}'.format(url))
    r = requests.get(url)
    if r.status_code == 200:
        with open(os.path.basename(url), 'wb') as file:
            file.write(r.content)
            return 'File {0} downloaded successfully'.format(url)
    else:
        return 'Error downloading file {0}'.format(url)

async def main(path, files):
    print('Downloading started')
    t = time.time()
    coroutines = [download(path + f) for f in files]
    completed, pending = await asyncio.wait(coroutines)
    for item in completed:
        print(item.result())
    print('Files downloaded in {0} seconds'.format(time.time() - t))

if __name__ == '__main__':
    path = 'http://www.irs.gov/pub/irs-pdf/'
    files = ['f1040.pdf', 'f1040a.pdf', 'f1040ez.pdf', 'f1040es.pdf', 'f1040sb.pdf']
    # download_files(path, files)

    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(main(path, files))
    event_loop.close()
