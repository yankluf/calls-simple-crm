// followUpCheck = document.getElementById('id_needs_follow_up')
// snippetContainer = document.getElementById('snippet-container')

// followUpCheck.addEventListener('change', () => {
//     if (followUpCheck.checked) {
//         fetch(`/form-snippet/?q=task`)
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error('Response wasn\'t OK!')
//             }
//             return response.text()
//         })
//         .then(data => {
//             snippetContainer.innerHTML = data
//         })
//         .catch(error => {
//             console.error('There was a problem getting the form: ', error)
//         })
//     } else if (!followUpCheck.checked) {
//         snippetContainer.innerHTML = ''
//     }
// })

window.addEventListener('DOMContentLoaded', () =>{
    localStorage.setItem('sidebarStatus', 'open')
    sidebarToggle = document.getElementById('sidebar-toggle')
    body = document.getElementById('app')

    sidebarToggle.addEventListener('click', () => {
        sidebarContent = document.getElementById('sidebar-content')

        if (localStorage.getItem('sidebarStatus') == 'closed') {
            sidebarContent.style.transition = 'all 150ms ease-in-out 100ms'
            sidebarContent.style.opacity = '1'
            body.style.gridTemplateColumns = '13% 3fr'
            localStorage.setItem('sidebarStatus', 'open')
        } else {
            body.style.gridTemplateColumns = '0% 3fr'
            localStorage.setItem('sidebarStatus', 'closed')
            sidebarContent.style.opacity = '0'
            sidebarContent.style.transition = 'all 150ms ease-in-out'
        }
    })
})

