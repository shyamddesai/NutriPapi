import Navbar from "../components/navbar";
import Header from "../components/index/header";
import Testimonials from "../components/index/testimonials";
import Footer from "../components/footer";
import styles from "./../css/index/index.module.css";

const LandingPage = () => {
  return (
    <div className={styles.landingpage}>
      <Navbar />
      {/* <Header />
      <section className={styles.midSection}>
        <div className={styles.mid} />
        <h2 className={styles.aSpecial1On1}>
          A special 1-on-1 recipe plan program that gives you complete control
          over your body for a perfect health
        </h2>
      </section>
      <Testimonials />
      <Footer /> */}
    </div>
  );
};

export default LandingPage;
