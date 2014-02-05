app = angular.module('ImanipApp', [])
	.config(['$routeProvider', '$locationProvider',
		function($routeProvider, $locationProvider) {
		$routeProvider
		.when('/', {
			templateUrl: '/static/partials/imanip.html'
		})
		.when('/image', {
			templateUrl: '/static/partials/display_image.html'
		})
		.otherwise({
			redirect_to: '/'
		});
	}])

app.directive('fileUpload', function () {
	return {
		scope: true,        //create a new scope
		link: function (scope, el, attrs) {
			el.bind('change', function (event) {
				var files = event.target.files;
				//iterate files since 'multiple' may be specified on the element
				for (var i = 0;i<files.length;i++) {
					scope.$emit("fileSelected", { file: files[i] });
				}                                       
			});
		}
	};
});