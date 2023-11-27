const express = require('express')
const app = express();
const mongoose = require('mongoose');
var routes = require('./routes/routes');
mongoose.set('strictQuery', false);

mongoose.connect("mongodb://localhost:27017/gbs",{useNewUrlParser: true,  useUnifiedTopology: true },function checkDb(error)

{
    if(error)
    {
        console.log("Error Connecting to DB");
    }
    else
    {
        console.log("successfully Connected to DB");
    }
});

app.listen(9002,function check(error)
{
    if(error)
    console.log("Error....!!!!");
    else
    console.log("Started....!!!!");
});


app.use(express.json());
app.use(routes);
