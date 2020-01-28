# coding: utf-8
import datetime
import json
import PyPDF2, hashlib
import requests
from flask import render_template, redirect
from random import randint

from app import app



# The node with which our application interacts, there can be multiple
# such nodes as well.
CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"

posts = []
i = 0


def fetch_posts():

    # Function to fetch the chain from a blockchain node, parse the data and store it locally.

    get_chain_address = "{}/chain".format(CONNECTED_NODE_ADDRESS)
    response = requests.get(get_chain_address)
    if response.status_code == 200:
        content = []
        chain = json.loads(response.content)
        for block in chain["chain"]:
            for tx in block["transactions"]:
                tx["index"] = block["index"]
                tx["hash"] = block["previous_hash"]
                content.append(tx)

        global posts
        posts = sorted(content, key=lambda k: k['timestamp'],
                       reverse=True)


@app.route('/')
def index():
    fetch_posts()
    return render_template('index.html',
                           title='YourNet: Decentralized '
                                 'content sharing',
                           posts=posts,
                           node_address=CONNECTED_NODE_ADDRESS,
                           readable_time=timestamp_to_string)


@app.route('/submit', methods=['POST'])

def submit_textarea():
    global i, hash, num_page
    count = 0
    count2 = 0
    block = ''
    content_block = []

    # Endpoint to create a new transaction via our application.

    pdf_file = open('INFO_Maupassant_Bel_Ami.pdf', 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)



    for x in range(read_pdf.numPages):

        content = read_pdf.getPage(x)
        num_page = read_pdf.getNumPages()
        text = content.extractText() + "\n"
        block += text
        count += 1
        count2 += 1

        if count == 5:
            content_block.append(block)
            hash = hashlib.sha256()
            hash.update(block.encode('UTF-8'))
            hash.hexdigest()
            count = 0
            block = ''

        elif count2 == read_pdf.numPages:
            content_block.append(block)
            hash = hashlib.sha256()
            hash.update(block.encode('UTF-8'))
            hash.hexdigest()

    contributor_id = randint(10000, 99999)
    post_object = {
        'author':  "UUID: "+ str(contributor_id),
        'content': content_block[i],
        'hash': hash.hexdigest(),
        'num_pages': num_page,
    }
    i +=1
    # Submit a transaction
    new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

    requests.post(new_tx_address,
                  json=post_object,
                  headers={'Content-type': 'application/json'})

    return redirect('/')


def timestamp_to_string(epoch_time):
    return datetime.datetime.fromtimestamp(epoch_time).strftime('%H:%M')



