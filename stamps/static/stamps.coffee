app = angular.module 'stamps', []

app.controller 'SearchCtrl', ($scope, $http) ->
    $scope.debug = false
    $scope.first = true
    $scope.results = {
        count: 0
    }
    $scope.stamps = []
    $scope.busy = true
    $scope.filters = {
        limit: 9,
        skip: 0
    }

    $scope.countries = []
    $scope.themes = []
    $scope.years = [2002..2014]
    $scope.years.unshift(null)

    $http.get('/api/countries').success (data) ->
        $scope.countries = data.countries
        $scope.countries.unshift(null)
        console.log(data)

    $http.get('/api/themes').success (data) ->
        $scope.themes = data.themes
        console.log(data)

    search = (clean) ->
        console.log('search', $scope.filters)
        $scope.busy = true
        $http.post('/api/search', $scope.filters).success (data) ->
            $scope.results = data
            if clean
                $scope.stamps = []
            for stamp in data.data
                $scope.stamps.push stamp
            $scope.busy = false
            if $scope.first
                console.log('first')
                $scope.first = false
                $scope.stamps = []
                $scope.filters.skip = Math.floor(Math.random() * data.count)
                search(true)

    $scope.next_page = () ->
        console.log('next page')
        if not $scope.busy and $scope.filters.skip < $scope.results.count - $scope.filters.limit
            $scope.filters.skip += $scope.filters.limit
            search(false)

    $scope.reset_search = () ->
        console.log('reset search')
        $scope.filters.skip = 0
        search(true)

    search(false)


app.directive 'whenScrolled', ($window) ->
    (scope, elm, attr) ->
        win = angular.element($window)
        body = document.body
        win.bind 'scroll', () ->
            top = body.scrollTop or document.documentElement.scrollTop
            if top + window.innerHeight >= body.scrollHeight - 100
                scope.next_page()


app.directive 'stamp', () ->
    restrict: 'E',
    templateUrl: '/templates/ministamp.slim',
    scope:
        stamp: '=',
