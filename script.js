const TODO_FILE = 'todo.txt'
const PARSED_TAG = '+parsed'
const CONTAINER_ELEMENT = 'linkContainer'

const getFileContent = (fileName) => fetch(fileName)
  .then(response => response.text())

const cleanUpLines = (rawLines) => rawLines
  .split(/\n/)
  .filter(line => line.length)

const getAllLines = getFileContent(TODO_FILE).then(fileContent => cleanUpLines(fileContent))

const filterSavedArticlesFromAllLines = getAllLines.then(lines => lines
  .filter(line => line.includes(PARSED_TAG))
)

const decodeHtml = (line) => {
  return new DOMParser().parseFromString(line, "text/html").documentElement.textContent;
}

filterSavedArticlesFromAllLines
  .then(lines => lines
    .map(line => {
      const splitBySpace = line.split(' ')
      const pageTitle = splitBySpace.slice(0, splitBySpace.length - 2).join(' ')
      const pageUrl = splitBySpace[splitBySpace.length - 2]

      const containerElement = document.getElementById(CONTAINER_ELEMENT)
      const listElement = document.createElement('li')
      const link = document.createElement('a')
      link.href = pageUrl
      link.textContent = decodeHtml(pageTitle)

      listElement.append(link)
      containerElement.append(listElement)
    })
  )
