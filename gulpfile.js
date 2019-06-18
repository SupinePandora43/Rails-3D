var gulp = require("gulp")
var jsonlint = require("gulp-jsonlint")

gulp.task("json", async () => {
    await gulp.src("./assets/**/*.json")
        .pipe(jsonlint())
        .pipe(jsonlint.failOnError())
        .pipe(jsonlint.reporter())
})
exports.default = gulp.series("json")