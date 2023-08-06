# -*- coding: utf-8 -*-

"""
“Commons Clause” License Condition v1.0
Copyright Oli 2019-2020
The Software is provided to you by the Licensor under the
License, as defined below, subject to the following condition.
Without limiting other conditions in the License, the grant
of rights under the License will not include, and the License
does not grant to you, the right to Sell the Software.
For purposes of the foregoing, “Sell” means practicing any or
all of the rights granted to you under the License to provide
to third parties, for a fee or other consideration (including
without limitation fees for hosting or consulting/ support
services related to the Software), a product or service whose
value derives, entirely or substantially, from the functionality
of the Software. Any license notice or attribution required by
the License must also include this Commons Clause License
Condition notice.
Software: PartyBot (fortnitepy-bot)
License: Apache 2.0

Fuck you.
"""

import sanic
import json
import datetime


class SanicServer:
    def __init__(self, client: "PartyBotClient") -> None:
        self.client = client
    
        self.sanic_app = sanic.Sanic('PartyBotClient', log_config={
            "version": 1,
            "sanic.root": {
                "level": "WARNING"
            }
        })
        self.server = None

        self.start_time = datetime.datetime.now()

    async def _route_main(self, request: sanic.request.Request) -> sanic.response.HTTPResponse:
        """
        {
            "route": "/"
        }
        """

        if not self.client.auth_error[0]:
            return sanic.response.html(f"""
            <head>
       <title>PartyBot</title>
       <link rel="stylesheet" media="all" href="https://dka575ofm4ao0.cloudfront.net/assets/status/status_manifest-243362a7df251188e1f8d87dbe67be112fc79c73d76c929231342a86f99a2f9c.css">
       <link rel="stylesheet" media="all" href="https://partybot.net/cdn/bot-style.css">
       <meta http-equiv="refresh" content="10">
    </head>
    <body class="status index status-none">
       <div class="layout-content status status-api">
          <div class="container">
             <div class="page-title">
                <div class="color-primary incident-name">{self.client.bot.user.display_name if self.client.bot.is_ready() else 'Bot starting...'}</div>
                <div class="font-largest color-secondary subheader">
                <img style="height: 25%" src="https://fortnite-api.com/images/cosmetics/br/{self.client.bot.party.me.outfit if self.client.bot.is_ready() else 'CID_VIP_Athena_Commando_M_GalileoGondola_SG'}/icon.png" />
                </div>
             </div>
             <div class="section">
                <div class="font-large">
                   Bot information:
                </div>
                <div class="font-small color-secondary description">
                   <p><b>Friends: </b> {len(self.client.bot.friends) if self.client.bot.is_ready() else 'N/A'}<br>
                   <b>Party Members ({self.client.bot.party.member_count - 1}):</b><br>
                   {"<br>".join([member.display_name for member in self.client.bot.party.members if member.display_name != self.client.bot.user.display_name] if self.client.bot.party.member_count != 1 else ['None.'])}
                </div>
             </div>
          </div>
       </div>
       </div>
    </body>
            """) if 'accept' not in request.headers or 'application/json' not in request.headers['accept'] else \
                sanic.response.json(
                    {
                        "online": self.client.bot.is_ready(),
                        "name": self.client.bot.user.display_name if self.client.bot.is_ready() else None,
                        "outfit": self.client.bot.party.me.outfit if self.client.bot.is_ready() else
                        "CID_VIP_Athena_Commando_M_GalileoGondola_SG",
                        "friends": len(self.client.bot.friends) if self.client.bot.is_ready() else 'N/A',
                        "party_members": [member.display_name for member in self.client.bot.party.members
                                          if member.display_name != self.client.bot.user.display_name]
                    },
                    status=200
                )
        else:
            return sanic.response.json(
                {
                    "error": "auth_invalid",
                    "message": self.client.auth_error[1]
                },
                status=503
            )

    async def _route_display_name(self, request: sanic.request.Request) -> sanic.response.HTTPResponse:
        """
        {
            "route": "/name"
        }
        """

        if self.client.bot.is_ready():
            return sanic.response.json(
                {
                    "display_name": self.client.bot.user.display_name
                }
            )
        else:
            return sanic.response.json(
                {
                    "error": "Bot hasn't started yet" if not self.client.auth_error[0] else "Bot will never start.",
                    "auth_error": self.client.auth_error[0]
                }
            )

    async def _route_uptime(self, request: sanic.request.Request) -> sanic.response.HTTPResponse:
        """
        {
            "route": "/uptime"
        }
        """
        try:
            return sanic.response.json(
                {
                    "uptime": str(datetime.datetime.now() - self.start_time).split('.')[:1][0]
                }
            )
        except Exception as e:
            print(e)

    async def register_routes(self) -> None:
        routes = dict((name, getattr(self, name)) for name in dir(self) if name.startswith('_route_'))

        for name, route in routes.items():
            endpoint = json.loads(route.__doc__)['route']
            self.sanic_app.add_route(route, endpoint)

    async def start_server(self) -> None:
        server = await self.sanic_app.create_server(
            port=80, host="0.0.0.0", return_asyncio_server=True
        )

        await server.startup()
        await server.serve_forever()
