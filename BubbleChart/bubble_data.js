var bubbleData = db.collection('chat');
chathistory.find().toArray(function (err, docs) {
    console.log(docs)
});