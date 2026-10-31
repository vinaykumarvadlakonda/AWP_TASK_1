#------------------------firebase index.html----------------------
<!DOCTYPE html>
<html lang="en">
<head>
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <title>Student Management System</title>
</head>
<body>
    <h1 class="text-primary text-center">Student Form </h1>
<form>
    <table class="table-secondary">

<tr>
    <td>Enter Student Name: <input type="text" name="name" id="name"><br><br>
</td>
</tr>

<tr>
    <td>Enter Student Roll Number: <input type="text" name="roll" id="roll"><br><br></td>
</tr>
<tr>
    <td>Enter Student Branch: <input type="text" name="branch" id="br"><br><br></td>
</tr>
<tr>
    <td>Enter Student Year: <input type="text" name="year" id="yr"><br><br></td>
</tr>

        
    
    <tr><td>Enter Student CGPA: <input type="text" name="cgpa" id="cg"><br><br></td></tr>
    

<tr><td> <input type="button" name="insert" value="INSERT" id="b1">
    <input type="button" name="delete" value="DELETE" id="b2">
    <input type="button" name="update" value="UPDATE" id="b3">
    <input type="button" name="display" value="DISPLAY" id="b4"></td></tr>
    </table>
</form>
    <!-- Firebase JavaScript SDK (v10 Module) -->
    <script type="module">
        import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
        import { getDatabase, ref, set, get, update, remove, child } 
            from "https://www.gstatic.com/firebasejs/10.8.0/firebase-database.js";

        // ⚠️ Replace this with YOUR Firebase Project Configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCpE6KPjYvKYh7gFqIW_qgU0iSJTYLmMNo",
  authDomain: "studentmn.firebaseapp.com",
  databaseURL: "https://studentmn-default-rtdb.firebaseio.com",
  projectId: "studentmn",
  storageBucket: "studentmn.firebasestorage.app",
  messagingSenderId: "40823612262",
  appId: "1:40823612262:web:cbcc8a0ac7b81b931cdea7",
  measurementId: "G-GTMPHR1E4G"
};

   // Initialize Firebase
        const app = initializeApp(firebaseConfig);
        const db = getDatabase(app);

        // --- Helper function to get form values ---
        function getFormData() {
            return {
                roll: document.getElementById('roll').value.trim(),
                name: document.getElementById('name').value.trim(),
                branch: document.getElementById('br').value.trim(),
                year: document.getElementById('yr').value.trim(),
                cgpa: document.getElementById('cg').value.trim()
            };
        }

        // --- 1. INSERT FUNCTION ---
        document.getElementById('b1').addEventListener('click', () => {
            const data = getFormData();
            if (!data.roll) {
                alert("Please enter Roll Number as it acts as the Student ID.");
                return;
            }

            set(ref(db, 'Students/' + data.roll), {
                name: data.name,
                branch: data.branch,
                year: data.year,
                cgpa: data.cgpa
            })
            .then(() => alert("Student Data Inserted Successfully!"))
            .catch((error) => alert("Error: " + error.message));
        });

        // --- 2. DELETE FUNCTION ---
        document.getElementById('b2').addEventListener('click', () => {
            const roll = document.getElementById('roll').value.trim();
            if (!roll) {
                alert("Enter Roll Number to delete student record.");
                return;
            }

            remove(ref(db, 'Students/' + roll))
                .then(() => alert("Student Data Deleted Successfully!"))
                .catch((error) => alert("Error: " + error.message));
        });

        // --- 3. UPDATE FUNCTION ---
        document.getElementById('b3').addEventListener('click', () => {
            const data = getFormData();
            if (!data.roll) {
                alert("Enter Roll Number to update record.");
                return;
            }

            update(ref(db, 'Students/' + data.roll), {
                name: data.name,
                branch: data.branch,
                year: data.year,
                cgpa: data.cgpa
            })
            .then(() => alert("Student Data Updated Successfully!"))
            .catch((error) => alert("Error: " + error.message));
        });

        // --- 4. DISPLAY (FETCH) FUNCTION ---
        document.getElementById('b4').addEventListener('click', () => {
            const roll = document.getElementById('roll').value.trim();
            if (!roll) {
                alert("Enter Roll Number to display data.");
                return;
            }

            const dbRef = ref(db);
            get(child(dbRef, `Students/${roll}`)).then((snapshot) => {
                if (snapshot.exists()) {
                    const student = snapshot.val();
                    document.getElementById('name').value = student.name || '';
                    document.getElementById('br').value = student.branch || '';
                    document.getElementById('yr').value = student.year || '';
                    document.getElementById('cg').value = student.cgpa || '';
                    alert("Data Retrieved Successfully!");
                } else {
                    alert("No student record found with Roll No: " + roll);
                }
            }).catch((error) => {
                alert("Error retrieving data: " + error.message);
            });
        });
    </script>
</body>
</html>

----------------os module ----------------
const os=require('os');
console.log("platform:",os.platform());
console.log("type:",os.type());
console.log("hostname:",os.hostname());
console.log("release:",os.release());
console.log("architecture:",os.arch());
console.log("total memory:",((os.totalmem())/1024/1024/1024).toFixed(2),"GB");
console.log("free memory:",(os.freemem()/1024/1024/1024).toFixed(2),"GB");

-----------http module-------------
var http = require('http');

var server = http.createServer(function(req, res) {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('<h1>Welcome to Node.js Web Server</h1>');
    res.write('<h2>Server Created Successfully!</h2>');
    res.end();
});

server.listen(3000, function() {
    console.log('Server running at http://localhost:3000/');
});

---------REST API server.js-------------
const express = require('express');
const app = express();

app.use(express.json());

let students = [
    {id: 1, name: "Rahul", branch: "CSE"},
    {id: 2, name: "Ravi", branch: "ECE"}
];

app.post('/students', (req, res) => {
    students.push(req.body);
    res.send("Student Added Successfully");
});

app.get('/students', (req, res) => {
    res.json(students);
});

app.put('/students/:id', (req, res) => {
    let id = parseInt(req.params.id);
    let student = students.find(s => s.id === id);

    if (student) {
        student.name = req.body.name;
        student.branch = req.body.branch;
        res.send("Student Updated Successfully");
    } else {
        res.send("Student Not Found");
    }
});

app.delete('/students/:id', (req, res) => {
    let id = parseInt(req.params.id);
    students = students.filter(s => s.id !== id);
    res.send("Student Deleted Successfully");
});

app.listen(3000, () => {
    console.log("REST API running at http://localhost:3000");
});

-----------fs module-----------------
const fs = require('fs');

fs.writeFileSync('student.txt',
    'Student Name: Rahul\nRoll Number: 101\nBranch: CSE\nYear: 2\nCGPA: 8.5');

console.log("File Created and Data Written Successfully");

const data = fs.readFileSync('student.txt', 'utf8');

console.log("Student Details:");
console.log(data);


---------path module-----------
const path = require('path');

const filePath = 'C:/Users/Student/Documents/student.txt';

console.log("Directory Name: " + path.dirname(filePath));
console.log("File Name: " + path.basename(filePath));
console.log("File Extension: " + path.extname(filePath));
console.log("Complete Path: " + path.resolve(filePath));

------------crud using express----------------
const express = require('express');
const app = express();

app.use(express.json());

let students = [];

app.post('/students', (req, res) => {
    students.push(req.body);
    res.send("Student Added Successfully");
});

app.get('/students', (req, res) => {
    res.json(students);
});

app.put('/students/:id', (req, res) => {
    let id = parseInt(req.params.id);
    let student = students.find(s => s.id === id);

    if (student) {
        student.name = req.body.name;
        student.branch = req.body.branch;
        student.cgpa = req.body.cgpa;
        res.send("Student Updated Successfully");
    } else {
        res.send("Student Not Found");
    }
});

app.delete('/students/:id', (req, res) => {
    let id = parseInt(req.params.id);
    students = students.filter(s => s.id !== id);
    res.send("Student Deleted Successfully");
});

app.listen(3000, () => {
    console.log("Server running at http://localhost:3000");
});

---------------jwt --------------

const express = require('express');
const jwt = require('jsonwebtoken');

const app = express();
app.use(express.json());

const SECRET_KEY = 'mysecretkey';

let students = [];

app.post('/login', (req, res) => {
    const { username, password } = req.body;

    if (username === 'admin' && password === '1234') {
        const token = jwt.sign({ username }, SECRET_KEY, {
            expiresIn: '1h'
        });
        res.json({ token });
    } else {
        res.status(401).send('Invalid Credentials');
    }
});

function verifyToken(req, res, next) {
    const header = req.headers['authorization'];

    if (!header) {
        return res.status(401).send('Access Denied');
    }

    const token = header.split(' ')[1];

    jwt.verify(token, SECRET_KEY, (err, decoded) => {
        if (err) {
            return res.status(403).send('Invalid Token');
        }
        req.user = decoded;
        next();
    });
}

app.post('/students', verifyToken, (req, res) => {
    students.push(req.body);
    res.send('Student Added Successfully');
});

app.get('/students', verifyToken, (req, res) => {
    res.json(students);
});

app.put('/students/:id', verifyToken, (req, res) => {
    const id = parseInt(req.params.id);
    const student = students.find(s => s.id === id);

    if (student) {
        student.name = req.body.name;
        student.branch = req.body.branch;
        student.cgpa = req.body.cgpa;
        res.send('Student Updated Successfully');
    } else {
        res.status(404).send('Student Not Found');
    }
});

app.delete('/students/:id', verifyToken, (req, res) => {
    const id = parseInt(req.params.id);
    const exists = students.some(s => s.id === id);

    if (exists) {
        students = students.filter(s => s.id !== id);
        res.send('Student Deleted Successfully');
    } else {
        res.status(404).send('Student Not Found');
    }
});

app.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});


--------------url module --------
const url = require('url');

const myURL = new URL('https://www.example.com:8080/student/details?name=Rahul&roll=101');

console.log("Protocol: " + myURL.protocol);
console.log("Hostname: " + myURL.hostname);
console.log("Pathname: " + myURL.pathname);
console.log("Query Parameters:");

myURL.searchParams.forEach((value, key) => {
    console.log(key + ": " + value);
});

---------react app for printing hello world------
app.js


import React from 'react';

function App() {
    return (
        <div>
            <h1>Hello World</h1>
        </div>
    );
}

export default App;


---------events module----------------
const EventEmitter = require('events');

const event = new EventEmitter();

event.on('studentRegistered', (name, roll) => {
    console.log("Student Registered Successfully!");
    console.log("Student Name: " + name);
    console.log("Roll Number: " + roll);
});

event.emit('studentRegistered', 'Rahul', 101);



---------------react to print date and time -------
---app.js

import React from 'react';

function App() {
    const date = new Date();

    return (
        <div>
            <h1>Current Date and Time</h1>
            <h2>Date: {date.toLocaleDateString()}</h2>
            <h2>Time: {date.toLocaleTimeString()}</h2>
        </div>
    );
}

export default App;

-----index.js-----------

import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(<App />);

-----------------custom module------
Math.js
function add(a, b) {
    return a + b;
}

function sub(a, b) {
    return a - b;
}

module.exports = { add, sub };

App.js


const math = require('./math');

console.log("Addition:", math.add(10, 5));
console.log("Subtraction:", math.sub(10, 5));

--------------react functional component----------------

app.js

import React from 'react';

function Student(props) {
    return (
        <div>
            <h2>Student Details</h2>
            <h3>Name: {props.name}</h3>
            <h3>Roll Number: {props.roll}</h3>
            <h3>Branch: {props.branch}</h3>
        </div>
    );
}

function App() {
    return (
        <div>
            <Student name="Rahul" roll="101" branch="CSE" />
            <Student name="Ravi" roll="102" branch="AIML" />
        </div>
    );
}

export default App;

-------------react class component that accepts input------

app.js

import React, { Component } from 'react';

class Student extends Component {
    render() {
        return (
            <div>
                <h2>Student Details</h2>
                <h3>Name: {this.props.name}</h3>
                <h3>Roll Number: {this.props.roll}</h3>
                <h3>Branch: {this.props.branch}</h3>
            </div>
        );
    }
}

class App extends Component {
    render() {
        return (
            <div>
                <Student name="Rahul" roll="101" branch="CSE" />
                <Student name="Ravi" roll="102" branch="AIML" />
            </div>
        );
    }
}

export default App;


-------class component that accepts date in the form of state-----------

import React, { Component } from 'react';

class DateDisplay extends Component {
    render() {
        return (
            <div>
                <h2>Current Date</h2>
                <h3>{this.props.date}</h3>
            </div>
        );
    }
}

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            date: new Date().toLocaleDateString()
        };
    }

    render() {
        return (
            <div>
                <h1>Date Display Application</h1>
                <DateDisplay date={this.state.date} />
            </div>
        );
    }
}

export default App;

---------------console module--------------
console.log("Student Information");
console.log("Name: Rahul");
console.log("Roll Number: 101");
console.log("Branch: CSE");
console.log("Year: 2");
console.log("CGPA: 8.5");

console.warn("Warning: Student attendance is low!");

console.error("Error: Student record not found!");

console.log("Program Executed Successfully");

------------------demonstrate component life cycle 

import React, { Component } from 'react';

class Student extends Component {

    constructor(props) {
        super(props);
        this.state = {
            name: 'Rahul'
        };
        console.log('Constructor Called');
    }

    componentDidMount() {
        console.log('Component Mounted');
    }

    componentDidUpdate() {
        console.log('Component Updated');
    }

    componentWillUnmount() {
        console.log('Component Unmounted');
    }

    render() {
        console.log('Render Called');

        return (
            <div>
                <h1>Student Details</h1>
                <h2>Name: {this.state.name}</h2>
                <button onClick={() => this.setState({name: 'Shiva'})}>
                    Update Name
                </button>
            </div>
        );
    }
}

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            show: true
        };
    }

    render() {
        return (
            <div>
                <button onClick={() => this.setState({show: !this.state.show})}>
                    Show / Hide Component
                </button>

                {this.state.show && <Student />}
            </div>
        );
    }
}

export default App;

----------using http and fs module ---------------
const fs = require('fs');
const http = require('http');

fs.writeFileSync('student.txt',
    'Student Name: Rahul\nRoll Number: 101\nBranch: CSE\nYear: 2\nCGPA: 8.5'
);

const server = http.createServer((req, res) => {
    fs.readFile('student.txt', 'utf8', (err, data) => {
        res.writeHead(200, {'Content-Type': 'text/plain'});

        if (err) {
            res.end('Error reading file');
        } else {
            res.end(data);
        }
    });
});

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});


--------------handle click events(good bye)=---------------
import React, { Component } from 'react';

class App extends Component {

    constructor(props) {
        super(props);
        this.state = {
            message: ''
        };
    }

    showDate() {
        this.setState({
            message: new Date().toLocaleString()
        });
    }

    render() {
        return (
            <div>
                <h1>React Event Handling</h1>

                <button onClick={this.showDate.bind(this)}>
                    Show Date and Time
                </button>

                <button onClick={() => this.setState({message: 'Good Bye'})}>
                    Say Goodbye
                </button>

                <h2>{this.state.message}</h2>
            </div>
        );
    }
}

export default App;

----fs and http to add and display student data---------------
const fs = require('fs');
const http = require('http');

const file = 'students.txt';

if (!fs.existsSync(file)) {
    fs.writeFileSync(file, '');
}

const server = http.createServer((req, res) => {

    if (req.url.startsWith('/add')) {
        const url = new URL(req.url, 'http://localhost:3000');

        const name = url.searchParams.get('name');
        const roll = url.searchParams.get('roll');
        const branch = url.searchParams.get('branch');

        const data = `Name: ${name}, Roll: ${roll}, Branch: ${branch}\n`;

        fs.appendFileSync(file, data);

        res.end('Student Added Successfully');
    }

    else if (req.url === '/students') {
        fs.readFile(file, 'utf8', (err, data) => {
            if (err) {
                res.end('Error Reading File');
            } else {
                res.writeHead(200, {'Content-Type': 'text/plain'});
                res.end(data || 'No Student Records Found');
            }
        });
    }

    else {
        res.writeHead(404);
        res.end('Page Not Found');
    }
});

server.listen(3000, () => {
    console.log('Server running at http://localhost:3000');
});

------------calculator application--------------

import React, { useState } from 'react';
import './App.css';

function App() {
    const [num1, setNum1] = useState('');
    const [num2, setNum2] = useState('');
    const [result, setResult] = useState('');

    const calculate = (op) => {
        let a = Number(num1);
        let b = Number(num2);

        if (num1 === '' || num2 === '') {
            setResult('Enter both numbers');
            return;
        }

        switch (op) {
            case '+':
                setResult(a + b);
                break;
            case '-':
                setResult(a - b);
                break;
            case '*':
                setResult(a * b);
                break;
            case '/':
                setResult(b !== 0 ? a / b : 'Cannot divide by zero');
                break;
            default:
                setResult('');
        }
    };

    return (
        <div className="container">
            <div className="calculator">
                <h1>React Calculator</h1>

                <input
                    type="number"
                    placeholder="Enter First Number"
                    value={num1}
                    onChange={(e) => setNum1(e.target.value)}
                />

                <input
                    type="number"
                    placeholder="Enter Second Number"
                    value={num2}
                    onChange={(e) => setNum2(e.target.value)}
                />

                <div className="buttons">
                    <button onClick={() => calculate('+')}>+</button>
                    <button onClick={() => calculate('-')}>-</button>
                    <button onClick={() => calculate('*')}>*</button>
                    <button onClick={() => calculate('/')}>/</button>
                </div>

                <h2>Result: {result}</h2>

                <button className="clear" onClick={() => {
                    setNum1('');
                    setNum2('');
                    setResult('');
                }}>
                    Clear
                </button>
            </div>
        </div>
    );
}

export default App;

--------------react registration page=---------------

app.js


import React, { useState } from 'react';
import './App.css';

function App() {
    const [form, setForm] = useState({
        name: '',
        email: '',
        password: '',
        branch: ''
    });

    const handleChange = (e) => {
        setForm({
            ...form,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        alert("Registration Successful!\nName: " + form.name);
    };

    return (
        <div className="container">
            <form onSubmit={handleSubmit}>
                <h1>Student Registration</h1>

                <input
                    type="text"
                    name="name"
                    placeholder="Enter Name"
                    value={form.name}
                    onChange={handleChange}
                    required
                />

                <input
                    type="email"
                    name="email"
                    placeholder="Enter Email"
                    value={form.email}
                    onChange={handleChange}
                    required
                />

                <input
                    type="password"
                    name="password"
                    placeholder="Enter Password"
                    value={form.password}
                    onChange={handleChange}
                    required
                />

                <select
                    name="branch"
                    value={form.branch}
                    onChange={handleChange}
                    required
                >
                    <option value="">Select Branch</option>
                    <option value="CSE">CSE</option>
                    <option value="AIML">AIML</option>
                    <option value="ECE">ECE</option>
                    <option value="EEE">EEE</option>
                </select>

                <button type="submit">Register</button>
            </form>
        </div>
    );
}

export default App;

