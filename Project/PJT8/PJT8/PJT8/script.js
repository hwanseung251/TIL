/**
 * 제공 코드
 */
// 기본 작가, 분류, 도서 데이터 (JavaScript Array)
const categories = categoryRawData
const authors = authorRawData
const books = bookRawData
// 데이터 확인
console.log(categories.length)
console.log(categories[0])
console.log(authors.length)
console.log(authors[0])
console.log(books.length)
console.log(books[0])

/**
 * 대부분의 작업은 script.js에서 진행해도 무방하나 원한다면 js 파일 추가 가능
 * HTML 요소 추가를 위한 `.innerHTML` 사용 금지, 요소의 내용을 비우는 용도로는 사용 가능 (`.innerHTML = ```)
 */


/* ===========================
 * 전역 상태
 * =========================== */

// 즐겨찾기된 도서들을 저장하는 Set (book 객체 자체를 저장)
let favoriteBooks = new Set()

// 현재 어떤 목록 모드인지: 'home' | 'favorites' | 'create'
let currentListMode = 'home'


/* ===========================
 * 공통 유틸 함수
 *  - 작가 / 분류 이름 찾기
 * =========================== */

// id -> author/category를 빠르게 찾기 위한 맵
let authorMap = new Map(authors.map(a => [a.id, a]))
let categoryMap = new Map(categories.map(c => [c.id, c]))

function getAuthorNameById(authorId) {
  const author = authorMap.get(authorId)
  return author ? author.name : ''
}

function getCategoryNameById(categoryId) {
  const category = categoryMap.get(categoryId)
  return category ? category.name : ''
}

function isFavorite(book) {
  return favoriteBooks.has(book)
}


/* ===========================
 * F01. 도서 목록 출력
 *  - #book-list-row 안에 Bootstrap Card로 렌더링
 *  - 반응형 그리드: col-12 / col-sm-6 / col-md-4 / col-lg-3
 *  - cover 없으면 stack-of-books.png 사용
 *  - F05: 카드에 즐겨찾기 버튼 추가
 * =========================== */

/**
 * 단일 도서 객체를 카드 형태로 만들어 반환하는 함수
 * @param {Object} book - bookRawData의 각 요소
 * @returns {HTMLElement} - col div (부트스트랩 그리드 한 칸)
 */
function createBookCard(book) {
  const col = document.createElement('div')
  col.classList.add('col-12', 'col-sm-6', 'col-md-4', 'col-lg-3')

  const card = document.createElement('div')
  card.classList.add('card', 'h-100')

  // 이미지
  const img = document.createElement('img')
  img.classList.add('card-img-top')
  let coverSrc = book.cover
  if (!coverSrc || String(coverSrc).trim() === '') {
    coverSrc = 'stack-of-books.png'
  }
  img.src = coverSrc
  img.alt = book.title || 'book cover'

  // 카드 바디
  const cardBody = document.createElement('div')
  cardBody.classList.add('card-body', 'd-flex', 'flex-column')

  const titleEl = document.createElement('h5')
  titleEl.classList.add('card-title')
  titleEl.textContent = book.title

  const metaEl = document.createElement('p')
  metaEl.classList.add('card-subtitle', 'mb-2', 'text-muted')
  const authorName = getAuthorNameById(book.authorId)
  const categoryName = getCategoryNameById(book.categoryId)
  metaEl.textContent = `${authorName} | ${categoryName}`

  const descEl = document.createElement('p')
  descEl.classList.add('card-text')
  descEl.textContent = book.description

  // 즐겨찾기 버튼 (F05)
  const favBtn = document.createElement('button')
  favBtn.type = 'button'
  favBtn.classList.add('btn', 'btn-sm', 'btn-outline-warning', 'mt-auto')

  function updateFavButtonLabel() {
    if (isFavorite(book)) {
      favBtn.textContent = '★ 즐겨찾기 해제'
    } else {
      favBtn.textContent = '☆ 즐겨찾기 추가'
    }
  }
  updateFavButtonLabel()

  favBtn.addEventListener('click', function (event) {
    // 카드 클릭 등 다른 이벤트와 섞이지 않도록
    event.stopPropagation()

    if (isFavorite(book)) {
      favoriteBooks.delete(book)
    } else {
      favoriteBooks.add(book)
    }

    updateFavButtonLabel()

    // 현재 Favorites 탭에서 즐겨찾기 해제한 경우 처리
    if (currentListMode === 'favorites') {
      if (favoriteBooks.size === 0) {
        // 즐겨찾기 비었으면 Home 탭으로 이동
        if (typeof window.showHomeTab === 'function') {
          window.showHomeTab()
        }
      } else {
        // 즐겨찾기 목록 다시 렌더
        const favArray = Array.from(favoriteBooks)
        renderBookList(favArray, '즐겨찾기한 도서가 없습니다.')
      }
    }
  })

  cardBody.appendChild(titleEl)
  cardBody.appendChild(metaEl)
  cardBody.appendChild(descEl)
  cardBody.appendChild(favBtn)

  card.appendChild(img)
  card.appendChild(cardBody)
  col.appendChild(card)

  return col
}

/**
 * 주어진 도서 배열을 #book-list-row에 렌더링하는 함수
 * @param {Array} bookList - 렌더링할 도서 배열
 * @param {string} [emptyMessage] - 목록이 비었을 때 표시할 메시지 (옵션)
 */
function renderBookList(bookList, emptyMessage) {
  const row = document.getElementById('book-list-row')
  if (!row) return

  // 이전 내용 초기화 (비우는 용도로 innerHTML 사용 허용)
  row.innerHTML = ''

  // 결과 없음 처리
  if (!bookList || bookList.length === 0) {
    const emptyDiv = document.createElement('div')
    emptyDiv.classList.add('col-12')

    const alertDiv = document.createElement('div')
    alertDiv.classList.add('alert', 'alert-secondary', 'mt-3')
    alertDiv.textContent = emptyMessage || '검색 결과가 없습니다.'

    emptyDiv.appendChild(alertDiv)
    row.appendChild(emptyDiv)
    return
  }

  bookList.forEach((book) => {
    const cardCol = createBookCard(book)
    row.appendChild(cardCol)
  })
}


/* ===========================
 * F02. 검색 기능
 * =========================== */

function setupSearch() {
  const searchForm = document.getElementById('search-form')
  const searchInput = document.getElementById('search-input')
  const searchFieldSelect = document.getElementById('search-field')
  const resetBtn = document.getElementById('search-reset-btn')

  if (!searchForm || !searchInput || !searchFieldSelect) {
    console.warn('검색 폼 요소를 찾을 수 없습니다. HTML id를 확인하세요.')
    return
  }

  searchForm.addEventListener('submit', function (event) {
    event.preventDefault()

    const keyword = searchInput.value.trim()
    const field = searchFieldSelect.value || 'title'

    if (keyword === '') {
      alert('검색어를 입력하세요.')
      searchInput.focus()
      return
    }

    const lowerKeyword = keyword.toLowerCase()

    const filtered = books.filter((book) => {
      if (field === 'title') {
        return String(book.title || '').toLowerCase().includes(lowerKeyword)
      }

      if (field === 'author') {
        const authorName = getAuthorNameById(book.authorId).toLowerCase()
        return authorName.includes(lowerKeyword)
      }

      if (field === 'category') {
        const categoryName = getCategoryNameById(book.categoryId).toLowerCase()
        return categoryName.includes(lowerKeyword)
      }

      return String(book.title || '').toLowerCase().includes(lowerKeyword)
    })

    currentListMode = 'home'  // 검색은 전체 목록 기준
    renderBookList(filtered, '검색 결과가 없습니다.')
  })

  if (resetBtn) {
    resetBtn.addEventListener('click', function () {
      searchInput.value = ''
      searchFieldSelect.value = 'title'
      currentListMode = 'home'
      renderBookList(books)
    })
  }
}


/* ===========================
 * F03 + F05. 탭 전환 (Home / Create / Favorites)
 * =========================== */

function setupTabs() {
  const homeNav = document.getElementById('home-nav')
  const createNav = document.getElementById('create-nav')
  const favoritesNav = document.getElementById('favorites-nav')
  const homeContainer = document.getElementById('home-container')
  const createContainer = document.getElementById('create-container')

  if (!homeNav || !createNav || !homeContainer || !createContainer) {
    console.warn('탭 관련 요소를 찾을 수 없습니다. id를 확인하세요.')
    return
  }

  // Home 탭 보여주기
  window.showHomeTab = function () {
    currentListMode = 'home'

    homeContainer.classList.remove('d-none')
    createContainer.classList.add('d-none')

    homeNav.classList.add('active')
    createNav.classList.remove('active')
    if (favoritesNav) favoritesNav.classList.remove('active')

    renderBookList(books)
  }

  // Create 탭 보여주기
  window.showCreateTab = function () {
    currentListMode = 'create'

    homeContainer.classList.add('d-none')
    createContainer.classList.remove('d-none')

    homeNav.classList.remove('active')
    createNav.classList.add('active')
    if (favoritesNav) favoritesNav.classList.remove('active')
  }

  // Favorites 탭 보여주기 (F05)
  window.showFavoritesTab = function () {
    currentListMode = 'favorites'

    homeContainer.classList.remove('d-none')
    createContainer.classList.add('d-none')

    homeNav.classList.remove('active')
    createNav.classList.remove('active')
    if (favoritesNav) favoritesNav.classList.add('active')

    const favArray = Array.from(favoriteBooks)
    renderBookList(favArray, '즐겨찾기한 도서가 없습니다.')
  }

  // 초기 상태: Home
  window.showHomeTab()

  homeNav.addEventListener('click', function () {
    window.showHomeTab()
  })

  createNav.addEventListener('click', function () {
    window.showCreateTab()
  })

  if (favoritesNav) {
    favoritesNav.addEventListener('click', function () {
      window.showFavoritesTab()
    })
  }
}


/* ===========================
 * F04. 도서 데이터 추가
 * =========================== */

function setupCreateForm() {
  const form = document.getElementById('create-form')
  const titleInput = document.getElementById('title-input')
  const authorInput = document.getElementById('author-input')
  const imgInput = document.getElementById('img-input')
  const descInput = document.getElementById('desc-input')
  const categoryInput = document.getElementById('category-input')
  const errorsUl = document.getElementById('create-book-errors')

  if (!form || !titleInput || !authorInput || !descInput || !categoryInput || !errorsUl) {
    console.warn('도서 추가 폼 요소를 찾을 수 없습니다. id를 확인하세요.')
    return
  }

  form.addEventListener('submit', function (event) {
    event.preventDefault()

    // 에러 초기화
    errorsUl.innerHTML = ''

    const title = titleInput.value.trim()
    const authorName = authorInput.value.trim()
    const imgUrlRaw = imgInput.value.trim()
    const description = descInput.value.trim()
    const categoryName = categoryInput.value.trim()

    const errors = []

    if (!title) errors.push('제목을 입력해주세요.')
    if (!authorName) errors.push('작가를 입력해주세요.')
    if (!description) errors.push('소개를 입력해주세요.')
    if (!categoryName) errors.push('분류를 입력해주세요.')

    if (errors.length > 0) {
      errors.forEach((msg) => {
        const li = document.createElement('li')
        li.textContent = msg
        li.classList.add('text-danger')
        errorsUl.appendChild(li)
      })
      return
    }

    // 이미지 URL 처리: http로 시작하지 않으면 빈 문자열
    let imgUrl = imgUrlRaw
    if (imgUrl && !imgUrl.startsWith('http')) {
      imgUrl = ''
    }

    // 작가 데이터 확인/추가
    let authorId = null
    let existingAuthor = Array.from(authorMap.values()).find(
      (a) => a.name === authorName
    )

    if (existingAuthor) {
      authorId = existingAuthor.id
    } else {
      const newAuthorId =
        authors.length > 0 ? Math.max(...authors.map((a) => a.id)) + 1 : 1

      const newAuthor = {
        id: newAuthorId,
        name: authorName,
      }

      authors.push(newAuthor)
      authorMap.set(newAuthorId, newAuthor)
      authorId = newAuthorId
    }

    // 분류 데이터 확인/추가
    let categoryId = null
    let existingCategory = Array.from(categoryMap.values()).find(
      (c) => c.name === categoryName
    )

    if (existingCategory) {
      categoryId = existingCategory.id
    } else {
      const newCategoryId =
        categories.length > 0 ? Math.max(...categories.map((c) => c.id)) + 1 : 1

      const newCategory = {
        id: newCategoryId,
        name: categoryName,
      }

      categories.push(newCategory)
      categoryMap.set(newCategoryId, newCategory)
      categoryId = newCategoryId
    }

    // 새 도서 객체 생성 (배열 맨 앞에 추가)
    const newBook = {
      title: title,
      description: description,
      cover: imgUrl,
      authorId: authorId,
      categoryId: categoryId,
    }

    books.unshift(newBook)

    // 폼 초기화
    titleInput.value = ''
    authorInput.value = ''
    imgInput.value = ''
    descInput.value = ''
    categoryInput.value = ''
    errorsUl.innerHTML = ''

    // Home 탭으로 이동 + 목록 재렌더링
    if (typeof window.showHomeTab === 'function') {
      window.showHomeTab()
    } else {
      currentListMode = 'home'
      renderBookList(books)
    }
  })
}


/* ===========================
 * 초기 실행
 * =========================== */

document.addEventListener('DOMContentLoaded', () => {
  // 탭 전환 (Home / Create / Favorites)
  setupTabs()

  // 검색 기능
  setupSearch()

  // 도서 추가 폼
  setupCreateForm()
})