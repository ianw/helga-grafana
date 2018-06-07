from helga.plugins.webhooks import route

channel = gettar(settings, 'GRAFANA_WEBHOOK_CHANNEL', None)

@route(r'/grafana', methods=['POST'])
def github_alerts(request, client):
    client.msg(channel, 'Testing grafana alerts!')
    return 'ok - message sent'
