<h1>Researcher-Village</h1>

<h3>Description</h3>
<p>
This web application built in Python with Flask. Registered students can create, update, and delete research project to-do lists that help keep track of project status, organize resources they are using for projects, categorize research topic, etc. Registered students can see other students projects and leave comments/ask questions/offer help.
</p>
<hr>
<h3>Controller Routes</h3>
<table>
  <thead>
      <tr>
          <td>Type</td>
          <td>Path</td>
          <td>Notes</td>
      </tr>
    <tbody>
        <tr>
            <td>GET</td>
            <td>/Path/Example</td>
            <td>Get example</td>
        </tr>
    </tbody>
</table>

<h2>Back-End</h2>
<h3>Schema</h3>
<h4>Users</h4>
<table>
  <thead>
      <tr>
          <td>Field</td>
          <td>Type</td>
          <td>Notes</td>
      </tr>
    <tbody>
        <tr>
            <td>id</td>
            <td>integer</td>
            <td>auto incremented primary key</td>
        </tr>
        <tr>
            <td>first_name</td>
            <td>VARCHAR(45)</td>
            <td>user first namey</td>
        </tr>
        <tr>
            <td>last_name</td>
            <td>VARCHAR(45)</td>
            <td>user last name</td>
        </tr>
        <tr>
            <td>class</td>
            <td>SET(...)</td>
            <td>user class</td>
        </tr>
        <tr>
            <td>email</td>
            <td>VARCHAR(45)</td>
            <td>user email address</td>
        </tr>
        <tr>
            <td>password</td>
            <td>VARCHAR(45)</td>
            <td>password hash</td>
        </tr>
        <tr>
            <td>created_at</td>
            <td>DATETIME</td>
            <td>record created date and time</td>
        </tr>
        <tr>
            <td>updated_at</td>
            <td>DATETIME</td>
            <td>record updated date and time</td>
        </tr>
    </tbody>
</table>
