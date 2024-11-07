// import { Chart } from "chart.js"
const root = document.getElementById('root')

const useFetch = async (path, method='GET', body='') => {
  const baseServerUrl = 'http://127.0.0.1:8080'
  let req = {
    method: method,
    headers: {
      "Content-Type": "application/json",
    },
    body : JSON.stringify(body)
  }
  if(method === 'GET') req = {method}
  const res = await fetch(baseServerUrl+path, req)
  return res.json()
}

const buildInsa = async () => {
  const loadedTestData = await useFetch('/')
  const div = document.createElement('div')
  div.innerText = loadedTestData
  root.append(div)
}

const postTest = async () => {
  const sendTest = await useFetch('/test', 'POST', '안녕하세요 브라우저에서 보냈어요')
  const { result } = sendTest
  const div = document.createElement('div')
  div.innerText = result
  root.append(div)
  
}

// const ctx = document.getElementById('myChart')

// new Chart(ctx, {
//   type: 'bar',
//   data: {
//     labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
//     datasets: [{
//       label: '# of Votes',
//       data: [12, 19, 3, 5, 2, 3],
//       borderWidth: 1
//     }]
//   },
//   options: {
//     scales: {
//       y: {
//         beginAtZero: true
//       }
//     }
//   }
// });


buildInsa()
postTest()