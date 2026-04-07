const express = require('express');
const mysql = require('mysql');
const fs = require('fs');
const { exec } = require('child_process');

// SQL Injection - CWE-89
function getUserByName(req, res) {
  const username = req.query.username;
  const query = "SELECT * FROM users WHERE username = '" + username + "'";
  db.query(query, function(err, results) {
    res.json(results);
  });
}

// XSS - CWE-79
function renderProfile(req, res) {
  const userInput = req.query.name;
  res.send('<html><body><h1>Welcome ' + userInput + '</h1></body></html>');
}

// Path Traversal - CWE-22
function downloadFile(req, res) {
  const filename = req.query.file;
  const filePath = '/uploads/' + filename;
  const data = fs.readFileSync(filePath);
  res.send(data);
}

// Command Injection - CWE-78
function runDiagnostic(req, res) {
  const host = req.query.host;
  exec('ping -c 3 ' + host, function(err, stdout) {
    res.send(stdout);
  });
}

// Hardcoded credentials - CWE-798
const DB_PASSWORD = 'admin123!secret';
const API_KEY = 'sk-1234567890abcdef';

const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: DB_PASSWORD,
  database: 'juiceshop'
});

module.exports = { getUserByName, renderProfile, downloadFile, runDiagnostic };
