# hello
import flask, json, sqlalchemy
import pandas as pd
flask_app = flask.Flask(__name__)
app_name = 'Pypup App'
app_nav = [ {'name': 'Home', 'page': 'main'} ]
tabls = {}
pages = {}
session = flask.session
settings = {
  'pp_users': False
}

SENDGRID_API_KEY = ''
flask_app.secret_key = 'BAD_SECRET_KEY'

# users

engine = sqlalchemy.create_engine('sqlite:///data.db?check_same_thread=False')
conn = engine.connect()
metadata = sqlalchemy.MetaData()

tables = {}
tables['users'] = sqlalchemy.Table('users', metadata,
              sqlalchemy.Column('id', sqlalchemy.Integer(),primary_key=True),
              sqlalchemy.Column('name', sqlalchemy.String(255), nullable=True),
              sqlalchemy.Column('email', sqlalchemy.String(255), nullable=False),
              sqlalchemy.Column('code', sqlalchemy.String(255), nullable=True)
              )

def create_tables():
  metadata.create_all(engine)

def get_or_create_user(email):
    ls_users= pd.read_sql(f'select * from users where email = "{email}"', conn).to_dict('records')
    if len(ls_users) == 0:
        conn.execute(tables['users'].insert().values(email=email))
    dt_user = pd.read_sql(f'select * from users where email = "{email}"', conn).to_dict('records')
    return dt_user[0]

def generate_code(dt_user):
    import random
    code = random.randrange(1,100000)
    send_email(from_email='ashish.singal1@gmail.com', 
        to_email=dt_user['email'], subject='Your code', 
        content=f'Your code is {code}')
    conn.execute(tables['users'].update().where(tables['users'].c.id == dt_user['id']).values(code=code))
    return True

def check_login(email, code):
    print(f'checking log in {email} {code}')
    ls_users = pd.read_sql(f'select * from users where email = "{email}" and code="{code}"', conn).to_dict('records')
    if len(ls_users) ==0: return False
    return ls_users[0]

def user(query_params):
    page = {'name': 'user', 'title': 'User Account', 'contents': []}
    page['contents'].append({'type': 'text', 'value':f'this is your account {flask.session["user"]["email"]}'})
    return page

def sign_out(query_params):
    page = {'name': 'sign_out', 'title': 'Sign Out', 'contents': []}
    flask.session.pop('user')
    page['contents'].append({'type': 'alert', 'text': f'you are signed out.'})
    return page

def sign_in(query_params):
    page = {'name': 'sign_in', 'title': 'Sign In', 'contents': []}
    form = { 'type': 'form', 'name': 'form', 'action': '?p=sign_in', 'contents': [] }
    print(query_params)
    if 'email' not in query_params:
        form['contents'].append({ 'type': 'formemail', 'name': 'email', 'label': 'Email' })
        form['contents'].append({ 'type': 'formsubmit', 'name': 'submit', 'label': 'Submit'})
    elif 'code' not in query_params:
        # get user from db
        dt_user = get_or_create_user(query_params['email'])
        generate_code(dt_user)
        form['contents'].append({ 'type': 'formhidden', 'name': 'email', 'label': 'Email', 'value': query_params['email'] })
        form['contents'].append({ 'type': 'formtext', 'name': 'code', 'label': 'Code' })
        form['contents'].append({ 'type': 'formsubmit', 'name': 'submit', 'label': 'Submit'})
    else:
        user = check_login(query_params['email'], query_params['code'])
        if user == False:
            page['contents'].append({'type': 'alert', 'text': f'failed to sign in'})
        else:
            flask.session['user'] = user
            page['contents'].append({'type': 'alert', 'text': f'you are signed in as {flask.session["user"]["email"]}'})
    page['contents'].append(form)
    return page


pages['sign_in'] = sign_in
pages['user'] = user

# end users

def send_email(from_email, to_email, subject, content):
  import sendgrid
  import os
  from sendgrid.helpers.mail import Mail, Email, To, Content

  sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
  mail = Mail(Email(from_email), To(to_email), subject, Content("text/plain", content))
  response = sg.client.mail.send.post(request_body=mail.get())
  print(response.status_code)
  print(response.body)
  print(response.headers)
  return True

def type_text(json):
  html = f"""<p>{json['value']}</p>"""
  return html

def type_hero(json):
    html = f"""  <div class="px-4 py-5 my-5 text-center">
    <!--<img class="d-block mx-auto mb-4" src="/docs/5.2/assets/brand/bootstrap-logo.svg" alt="" width="72" height="57">-->
    <h1 class="display-5 fw-bold">{json['title']}</h1>
    <div class="col-lg-6 mx-auto">
      <p class="lead mb-4">{json['text']}</p>
      <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
        <button type="button" class="btn btn-primary btn-lg px-4 gap-3">{json['primary']}</button>
        <button type="button" class="btn btn-outline-secondary btn-lg px-4">{json['secondary']}</button>
      </div>
    </div>
  </div>"""
    return html

def set_defaults(json_defaults, json):
  return json_defaults | json

def type_card(json):
  html = """
  <div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>"""
  return html

def type_card_group(json):
  import math
  card_count = len(json['cards'])
  cards_per_row = 2
  rows = math.ceil(card_count / float(cards_per_row))
  html = ''
  for r in range(rows):
    print(f'row {r}')
    html += """<div class="row">"""
    for c in range(cards_per_row):
      card_index = r * cards_per_row + c
      html += type_card(json['cards'][card_index])
    html += "</div>"
  return html

def type_form(json):
    json = set_defaults ({'action': '?p=main'}, json)
    html = f"""<form action="/{json['action']}" method="post">"""
    return html

def type_formselect(json):
    html = """
    <select class="form-select" aria-label="Default select example">
      <option selected>Open this select menu</option>
      <option value="1">One</option>
      <option value="2">Two</option>
      <option value="3">Three</option>
    </select>"""
    return html

def type_alert(json):
    print('why am i called twice')
    html = f"""<div class="alert alert-primary" role="alert">{json['text']}</div>"""
    return html

def type_header(json):
    size = 1
    if 'size' in json: size = json['size']
    html = f'<h{size}>' + json['text'] + '</h{size}>'
    return html

def type_formtext(json):
    json = set_defaults({'label': json['name'], 'name': 'text', 'value': ''}, json)
    html = f"""<div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label">{json['label']}</label>
      <input name="{json['name']}" type="text" class="form-control" id="{json['name']}" value="{json['value']}">
    </div>"""
    return html

def type_formhidden(json):
    json = set_defaults({'name': 'text'}, json)
    html = f"""
      <input name="{json['name']}" type="hidden" id="{json['name']}" value="{json['value']}">"""
    return html

def type_formemail(json):
    json = set_defaults({'label': 'Email', 'name': 'email', 'value': ''}, json)
    html = f"""<div class="mb-3">
      <label for="exampleFormControlInput1" class="form-label">{json['label']}</label>
      <input name="{json['name']}" type="email" class="form-control" id="{json['name']}" placeholder="name@example.com"  value="{json['value']}">
    </div>"""
    return html

def type_formtextarea(json):
    json = set_defaults({'label': json['name'], 'name': 'Text', 'value': ''}, json)
    html = f"""
    <div class="mb-3">
      <label for="exampleFormControlTextarea1" class="form-label">{json['label']}</label>
      <textarea class="form-control" id="{json['name']}" name="{json['name']}" rows="3"> {json['value']}</textarea>
    </div>"""
    return html

def type_formsubmit(json):
    html = """<input type="submit" value="submit" name="submit">"""
    return html

def js_aggrid(df, jsid, col_defs={}):
    json_col_defs = '[ '
    
    for c in list(df.columns):
        jc = f""" {{
            headerName: "{c}",
            field: "{c}", 
            """
        if c in col_defs:
            if col_defs[c].get('html') == True:
                jc = jc + """ 
                cellRenderer: function(params) {
                            return params.value ? params.value : '';
                        }, 
                        """
            if 'format' in col_defs[c]:
                if col_defs[c]['format'] == 'pct':
                    jc = jc + """
                    valueFormatter: params => { return (parseFloat(params.value).toFixed(2)+"%"); },
                    """
        jc = jc + '}, '
        json_col_defs = json_col_defs + jc
    json_col_defs = json_col_defs + '] '
        
    # json_col_defs = json.dumps([{'headerName': c, 'field':c } for c in list(df.columns)])
    json_row_data = json.dumps(df.to_dict(orient='records'))
    js = f"""
        var columnDefs{jsid} = {json_col_defs};
        var rowData{jsid} = {json_row_data};
        var gridOptions{jsid} = {{
          columnDefs: columnDefs{jsid},
          rowData: rowData{jsid}
        }};
        document.addEventListener('DOMContentLoaded', function() {{
          var gridDiv{jsid} = document.querySelector('#divid_aggrid_{jsid}');
          new agGrid.Grid(gridDiv{jsid}, gridOptions{jsid});
}});
    """
    return js

def type_aggrid(json):
    html = ''
    html += """<script>""" + js_aggrid(json['df'], json['jsid'], json['col_defs']) + """</script>"""
    html+= f"""
      <div id="divid_aggrid_{json['jsid']}" style="height: 200px;" class="ag-theme-balham"></div>
    """
    return html

def js_plotly(df, x, y, jsid):
    json_x = json.dumps(list(df[x]))
    json_y = json.dumps(list(df[y]))
    return f"""
          var data{jsid} = [
  {{
    x: {json_x},
    y: {json_y},
    type: 'bar',
    marker: {{
        color: '#BB3E03'
    }}
  }}
];
Plotly.newPlot('divid_plotly_{jsid}', data{jsid}, {{autosize: true, height: 200, 
  margin: {{
    l: 10,
    r: 10,
    b: 10,
    t: 10,
    pad: 4
  }}, 
  paper_bgcolor: '#ffffff',
  plot_bgcolor: '#ffffff' }});
"""

def type_plotly(json):
    html = ''
    html+= f"""
      <div id="divid_plotly_{json['jsid']}" style="height: 200px;"></div>
    """
    html += """<script>""" + js_plotly(json['df'], json['x'], json['y'], json['jsid']) + """</script>"""
    return html

def make_link(txt, href):
    return f'<a target="_blank" href="https://www.{href}.com">{txt}</a>'



def page_contents(contents, html = ''):
    for content in contents:
        # need start html and end html
        print(content)
        print(f'type_' + content['type'] + '(content)')
        html += eval(f'type_' + content['type'] + '(content)')
        if 'contents' in content:
            html += page_contents(content['contents'], html)
    return html

def build_page(page_json):
    jinja_vars = {}
    jinja_vars['page_title'] = page_json['title']
    print(page_json)
    html = page_contents(page_json['contents'])
    jinja_vars['html'] = html
    jinja_vars['app_name'] = app_name
    return jinja_vars

@flask_app.route('/',methods = ['POST', 'GET'])
def main():
    query_params = flask.request.args.to_dict() | flask.request.form.to_dict()
    page = 'main'
    if 'p' in query_params: page = query_params['p']
    page_json = pages[page](query_params)
    jinja_vars = build_page(page_json)
    return flask.render_template('bootstrap.html', jinja_vars=jinja_vars)

@flask_app.route('/test')
def test():
    query_params = flask.request.args.to_dict()
    return flask.render_template(f'{query_params["template"]}.html')

def run():
    flask_app.run(debug=True, host='0.0.0.0', port=5000)