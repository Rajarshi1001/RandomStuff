const express = require('express');
const mongoose = require('mongoose');
const schema = mongoose.Schema

const UserSchema = new mongoose.Schema({
    firstname: {
      type: String,
      required: true
    },
    lastname: {
        type: String,
        required: true
    },
    date: {
      type: Date,
      default: Date.now
    }
  });
module.exports = mongoose.model('Users', UserSchema);