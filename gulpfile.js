var gulp = require("gulp")
var jsonlint = require("gulp-jsonlint")
var zip = require("gulp-zip")
// RegExp(/[.]\/assets\/**\/*.json/gim)
gulp.task("json", async () => {
	await gulp.src(["./assets/**/*.json", "pack.mcmeta"])
		.pipe(jsonlint())
		.pipe(jsonlint.failOnError())
		.pipe(jsonlint.reporter())
})
gulp.task("zip", async () => {
	await gulp.src(["**/assets/**", "pack.*"])
		.pipe(zip("rails-3d.zip", { compress: false }))
		.pipe(gulp.dest("."))
})
exports.default = gulp.series("json", "zip")