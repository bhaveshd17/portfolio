function sendEmail() {
  const msg = document.getElementById('msg')
  window.open('mailto:bhaveshdhake4@gmail.com?subject=Want To Contact&body='+msg.value)
}
